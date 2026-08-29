#!/usr/bin/env python3
"""
Inline a static site's CSS, JS and local images into one self-contained HTML
file, for a fast preview via SendUserFile or the Artifact tool.

Written for website-studio phase 4/5, so this never gets hand-rolled again
per project. Usage:

    python3 preview.py <site_dir> <out_file> [--title "Name"]

<site_dir> is expected to contain index.html, and whatever assets/css,
assets/js and assets/img files it links to via relative paths starting with
"assets/". Anything else (Google Fonts links, CDN scripts) is left alone —
those are fetched by the viewer's browser directly and are already
Artifact-CSP-safe per artifact-design.

Produces two things depending on --mode:
  full   (default) — a standalone HTML file with <!DOCTYPE>/<html>/<body>,
          for SendUserFile. Open it directly in a browser.
  artifact — strips the outer <!DOCTYPE>/<html>/<head>/<body> wrapper per
          the Artifact tool's content rules (title + style at top, no outer
          document tags), for publishing with the Artifact tool.
"""

import argparse
import base64
import mimetypes
import re
import sys
from pathlib import Path


def inline_asset_refs(html: str, site_dir: Path) -> str:
    """Replace assets/css/*.css and assets/js/*.js references with inline
    <style>/<script> blocks, and assets/img/* references with data URIs."""

    def read(rel: str) -> str:
        return (site_dir / rel).read_text(encoding="utf-8")

    # <link rel="stylesheet" href="assets/css/whatever.css">
    def css_sub(m: re.Match) -> str:
        rel = m.group("href")
        if not rel.startswith("assets/"):
            return m.group(0)  # leave Google Fonts etc. alone
        return f"<style>\n{read(rel)}\n</style>"

    html = re.sub(
        r'<link[^>]+rel="stylesheet"[^>]+href="(?P<href>assets/[^"]+\.css)"[^>]*>',
        css_sub,
        html,
    )

    # <script src="assets/js/whatever.js"></script>
    def js_sub(m: re.Match) -> str:
        rel = m.group("src")
        if not rel.startswith("assets/"):
            return m.group(0)  # leave CDN scripts alone
        return f"<script>\n{read(rel)}\n</script>"

    html = re.sub(
        r'<script[^>]+src="(?P<src>assets/[^"]+\.js)"[^>]*></script>',
        js_sub,
        html,
    )

    # Any assets/img/* reference, in src="" or url() or og:image content=""
    def img_sub(m: re.Match) -> str:
        rel = m.group(0)
        path = site_dir / rel
        if not path.exists():
            return rel
        mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        b64 = base64.b64encode(path.read_bytes()).decode()
        return f"data:{mime};base64,{b64}"

    html = re.sub(r"assets/img/[^\s\"')]+", img_sub, html)

    return html


def to_artifact_body(html: str, title_override: str | None) -> str:
    """Strip outer document tags per the Artifact tool's content rules:
    no <!DOCTYPE>, <html>, <head>, or <body> — title and style at the top."""
    body_match = re.search(r"<body[^>]*>(.*)</body>", html, re.S)
    body = body_match.group(1) if body_match else html

    if title_override:
        title = title_override
    else:
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        title = t.group(1).strip() if t else "Preview"

    return f"<title>{title}</title>\n{body.strip()}\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("site_dir", type=Path)
    ap.add_argument("out_file", type=Path)
    ap.add_argument("--entry", default="index.html", help="HTML file to start from")
    ap.add_argument("--mode", choices=["full", "artifact"], default="full")
    ap.add_argument("--title", default=None, help="Override <title> (artifact mode)")
    args = ap.parse_args()

    entry = args.site_dir / args.entry
    if not entry.exists():
        sys.exit(f"error: {entry} not found")

    html = entry.read_text(encoding="utf-8")
    html = inline_asset_refs(html, args.site_dir)

    if args.mode == "artifact":
        html = to_artifact_body(html, args.title)

    args.out_file.parent.mkdir(parents=True, exist_ok=True)
    args.out_file.write_text(html, encoding="utf-8")
    size_kb = args.out_file.stat().st_size / 1024
    print(f"wrote {args.out_file} ({size_kb:.0f} KB, mode={args.mode})")


if __name__ == "__main__":
    main()
