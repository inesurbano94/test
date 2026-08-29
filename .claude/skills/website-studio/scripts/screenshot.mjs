#!/usr/bin/env node
/**
 * Render an HTML file headless and screenshot it, so a build or edit gets
 * actually looked at before it's called done — not just checked for
 * non-empty output. check.py inspects source; this inspects what a
 * browser actually paints, which is the only thing that would have caught
 * a real bug shipped once: preview.py's artifact mode silently dropping
 * every <style> block. A script producing screenshots doesn't replace
 * looking at them — read the PNGs this writes before calling anything done.
 *
 * Accepts either a full HTML document, or an artifact-mode fragment
 * (preview.py --mode artifact output, no <html>/<head>/<body>) — the
 * fragment gets auto-wrapped in a minimal shell so it renders the same
 * way the Artifact viewer would.
 *
 * Usage:
 *   node screenshot.mjs <html_file> <out_dir> [--label name] [--widths 1280,390] [--wait 1200]
 *
 * Writes <out_dir>/<label>-<width>.png for each width and prints any
 * console/page errors found. Uses the environment's own Playwright/Chromium
 * config (PLAYWRIGHT_BROWSERS_PATH) with no hardcoded browser path — that
 * broke once already when a pinned version string went stale. Only adds a
 * proxy if HTTPS_PROXY is actually set in the environment, so this stays
 * portable to environments that don't need one.
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "fs";
import { basename, resolve } from "path";

// Try a bare import first (works if node_modules is actually in scope);
// fall back to this environment's known global install. Bare import tried
// first so this keeps working unmodified in an environment set up more
// conventionally than this one.
let chromium;
try {
  ({ chromium } = await import("playwright"));
} catch {
  ({ chromium } = await import("/opt/node22/lib/node_modules/playwright/index.mjs"));
}

function parseArgs(argv) {
  const args = { widths: "1280,390", wait: "1200", label: null };
  const positional = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--widths") args.widths = argv[++i];
    else if (a === "--wait") args.wait = argv[++i];
    else if (a === "--label") args.label = argv[++i];
    else positional.push(a);
  }
  args.htmlFile = positional[0];
  args.outDir = positional[1];
  return args;
}

const args = parseArgs(process.argv.slice(2));
if (!args.htmlFile || !args.outDir) {
  console.error("usage: node screenshot.mjs <html_file> <out_dir> [--label name] [--widths 1280,390] [--wait 1200]");
  process.exit(1);
}
// Resolve to absolute paths — a relative path produces an invalid file://
// URL, not a "file not found" you'd notice before it's too late.
args.htmlFile = resolve(args.htmlFile);
args.outDir = resolve(args.outDir);

const label = args.label || basename(args.htmlFile).replace(/\.html?$/, "");
const widths = args.widths.split(",").map((w) => parseInt(w.trim(), 10));
const wait = parseInt(args.wait, 10);

if (!existsSync(args.outDir)) mkdirSync(args.outDir, { recursive: true });

let raw = readFileSync(args.htmlFile, "utf8");
const isFragment = !/<html[\s>]/i.test(raw);
const fileUrl = "file://" + (isFragment ? writeWrapped(raw) : args.htmlFile);

function writeWrapped(fragment) {
  const wrapped = `<!doctype html><html><head><meta charset="utf-8"></head><body>${fragment}</body></html>`;
  const path = args.htmlFile.replace(/\.html?$/, "") + ".wrapped-for-screenshot.html";
  writeFileSync(path, wrapped, "utf8");
  return path;
}

const launchOpts = { headless: true };
if (process.env.HTTPS_PROXY || process.env.https_proxy) {
  launchOpts.proxy = { server: process.env.HTTPS_PROXY || process.env.https_proxy };
  launchOpts.args = ["--ignore-certificate-errors"];
}

const browser = await chromium.launch(launchOpts);
let anyErrors = false;

for (const width of widths) {
  const page = await browser.newPage({ viewport: { width, height: Math.round(width * 1.1) } });
  const errors = [];
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error") errors.push("console: " + m.text()); });

  await page.goto(fileUrl, { waitUntil: "load" });
  await page.waitForTimeout(wait);

  const outPath = `${args.outDir}/${label}-${width}.png`;
  await page.screenshot({ path: outPath, fullPage: width >= 1200 ? false : true });

  console.log(`wrote ${outPath}`);
  if (errors.length) {
    anyErrors = true;
    console.log(`  ${errors.length} error(s) at ${width}px:`);
    errors.slice(0, 5).forEach((e) => console.log(`    ${e}`));
  }
  await page.close();
}

await browser.close();

if (isFragment) {
  console.log(`(rendered as a wrapped fragment — this is artifact-mode content, not a standalone page)`);
}
if (anyErrors) {
  console.log("\nErrors were found — read them before deciding this is fine.");
}
console.log(`\nNow use Read on the PNG(s) above. A script printing "0 errors" is not the same as having looked.`);
