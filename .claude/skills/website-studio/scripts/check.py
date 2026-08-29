#!/usr/bin/env python3
"""
Static pre-flight checks for a website-studio build. Run at phase 5,
before the manual read of qa.md — this catches the mechanical things
faster and more reliably than eyeballing the checklist does.

This is a heuristic lint on source files, not a browser: it cannot see
layout, real computed contrast in a rendered page, or runtime console
errors on a published page. Pair it with scripts/screenshot.mjs, which
renders the actual output headless — the two are complementary, not
alternatives. This one would not have caught the artifact-mode CSS bug
(the source file was fine; what got published wasn't) — screenshot.mjs
would have and now does, that's why both exist.

Usage:
    python3 check.py <site_dir> [--entry index.html]

Exit code is 0 if nothing failed, 1 if any check failed.
"""

import argparse
import re
import sys
from pathlib import Path

FAIL = "FAIL"
WARN = "WARN"
OK = "OK"

# Phrases banned in taste.md's "vague premium copy" ban. Keep in sync by
# hand — this list is intentionally small and specific, not a generic
# marketing-cliche detector.
VAGUE_COPY = [
    "elevate your", "where quality meets", "your journey starts",
    "excellence in", "passion for excellence", "unparalleled",
    "state-of-the-art", "take it to the next level", "best-in-class",
]

PLACEHOLDER_MARKERS = [
    "351900000000", "WHATSAPP_NUMBER =", "[headline here]", "lorem ipsum",
    "TODO", "PLACEHOLDER",
]


def hex_to_rgb(h: str):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def relative_luminance(rgb) -> float:
    def chan(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex_a: str, hex_b: str):
    a, b = hex_to_rgb(hex_a), hex_to_rgb(hex_b)
    if not a or not b:
        return None
    la, lb = relative_luminance(a), relative_luminance(b)
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


def load_tokens(css: str) -> dict:
    tokens = {}
    for name, val in re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3,8})\s*;", css):
        tokens[name] = val
    return tokens


def check_contrast(css: str, results: list) -> None:
    tokens = load_tokens(css)
    if not tokens:
        results.append((WARN, "contrast", "no hex tokens found in :root — skipped"))
        return

    # Heuristic pairs: text-role tokens over ground-role tokens, matched by
    # naming convention across the four seeded design systems.
    text_roles = [n for n in tokens if n in ("ink", "ink-soft", "text", "text-soft")]
    ground_roles = [n for n in tokens if n in ("ground", "paper", "cream", "raised", "white", "off")]

    if not text_roles or not ground_roles:
        results.append((WARN, "contrast", "couldn't infer text/ground token pairs — check by hand"))
        return

    for t in text_roles:
        for g in ground_roles:
            ratio = contrast_ratio(tokens[t], tokens[g])
            if ratio is None:
                continue
            level = FAIL if ratio < 4.5 else (WARN if ratio < 4.5 else OK)
            label = f"--{t} on --{g} = {ratio:.2f}:1"
            if ratio < 4.5:
                results.append((FAIL, "contrast", f"{label} — below 4.5:1 body-text minimum"))
            else:
                results.append((OK, "contrast", label))


def check_html(html: str, results: list) -> None:
    if not re.search(r"<html[^>]+lang=", html):
        results.append((FAIL, "html", "<html> missing lang attribute"))
    else:
        results.append((OK, "html", "<html lang> present"))

    if not re.search(r"<title>.+?</title>", html, re.S):
        results.append((FAIL, "html", "<title> missing or empty"))
    if not re.search(r'<meta name="description" content="[^"]+"', html):
        results.append((FAIL, "html", "meta description missing"))
    if not re.search(r'<meta property="og:title"', html):
        results.append((WARN, "html", "og:title missing — link previews will look bare"))
    if not re.search(r'<link rel="icon"', html):
        results.append((WARN, "html", "no favicon link found"))

    if len(re.findall(r"<h1[\s>]", html)) != 1:
        results.append((WARN, "html", f"expected exactly one <h1>, found {len(re.findall(r'<h1[ >]', html))}"))

    imgs = re.findall(r"<img\b[^>]*>", html)
    missing_alt = [i for i in imgs if "alt=" not in i]
    if missing_alt:
        results.append((FAIL, "html", f"{len(missing_alt)} <img> tag(s) missing alt="))
    elif imgs:
        results.append((OK, "html", f"all {len(imgs)} <img> tags have alt="))

    # anchor links resolve to a real id
    hrefs = set(re.findall(r'href="#([\w-]+)"', html))
    hrefs.discard("")
    ids = set(re.findall(r'id="([\w-]+)"', html))
    broken = hrefs - ids
    if broken:
        results.append((FAIL, "html", f"anchor(s) with no matching id: {', '.join(sorted(broken))}"))
    elif hrefs:
        results.append((OK, "html", f"all {len(hrefs)} anchor links resolve"))


def check_seo(html: str, site_dir: Path, results: list) -> None:
    if not re.search(r'<link rel="canonical" href="[^"]+"', html):
        results.append((WARN, "seo", "no canonical <link> — add once the real published URL is known"))
    else:
        results.append((OK, "seo", "canonical link present"))

    if (site_dir / "sitemap.xml").exists():
        results.append((OK, "seo", "sitemap.xml present"))
    else:
        results.append((WARN, "seo", "no sitemap.xml in project root"))

    if (site_dir / "robots.txt").exists():
        results.append((OK, "seo", "robots.txt present"))
    else:
        results.append((WARN, "seo", "no robots.txt in project root"))

    ld_blocks = re.findall(r'<script[^>]+type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S)
    types_found = set()
    for block in ld_blocks:
        for t in re.findall(r'"@type"\s*:\s*"([^"]+)"', block):
            types_found.add(t)
    if not ld_blocks:
        results.append((WARN, "seo", "no JSON-LD structured data found — add LocalBusiness if this business has an address/service area"))
    else:
        results.append((OK, "seo", f"JSON-LD present ({', '.join(sorted(types_found)) or len(ld_blocks)} block(s))"))

    has_faq_section = bool(re.search(r'id="faq"', html, re.I))
    if has_faq_section and "FAQPage" not in types_found:
        results.append((WARN, "seo", "site has an FAQ section but no FAQPage JSON-LD — free rich-snippet real estate going unused"))


def check_css(css: str, results: list) -> None:
    if "prefers-reduced-motion" not in css:
        results.append((FAIL, "motion", "no prefers-reduced-motion rule in CSS"))
    else:
        results.append((OK, "motion", "prefers-reduced-motion present"))

    if "focus-visible" not in css:
        results.append((FAIL, "interaction", "no :focus-visible rule in CSS"))
    else:
        results.append((OK, "interaction", ":focus-visible present"))

    # crude purple/blue-gradient-glow tell from taste.md's banned list
    gradients = re.findall(r"linear-gradient\([^)]*\)|radial-gradient\([^)]*\)", css)
    for g in gradients:
        hexes = re.findall(r"#[0-9a-fA-F]{3,8}", g)
        for h in hexes:
            rgb = hex_to_rgb(h)
            if rgb and rgb[2] > rgb[0] + 30 and rgb[2] > rgb[1] + 10:
                results.append((WARN, "taste", f"blue/purple-leaning gradient stop {h} — check against the banned list in taste.md"))
                break


def check_copy(html: str, results: list) -> None:
    text = re.sub(r"<[^>]+>", " ", html).lower()
    hits = [p for p in VAGUE_COPY if p in text]
    if hits:
        results.append((FAIL, "copy", f"vague premium phrase(s) found: {', '.join(hits)}"))
    else:
        results.append((OK, "copy", "no banned vague-copy phrases found"))

    # emoji used as a section marker/icon — crude but catches the common case
    emoji_near_heading = re.findall(r"<h[1-3][^>]*>[^<]{0,4}([\U0001F300-\U0001FAFF☀-➿])", html)
    if emoji_near_heading:
        results.append((WARN, "taste", f"emoji next to a heading — check it isn't standing in as an icon: {emoji_near_heading}"))


def check_placeholders(html: str, js: str, results: list) -> None:
    combined = html + "\n" + js
    hits = [p for p in PLACEHOLDER_MARKERS if p in combined]
    if hits:
        results.append((WARN, "handover", f"placeholder marker(s) still present, confirm README covers them: {', '.join(sorted(set(hits)))}"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("site_dir", type=Path)
    ap.add_argument("--entry", default="index.html")
    args = ap.parse_args()

    entry = args.site_dir / args.entry
    if not entry.exists():
        sys.exit(f"error: {entry} not found")

    # Strip HTML comments first - a comment that mentions example markup
    # (e.g. explaining what an <img> tag should look like) would otherwise
    # be scanned as if it were real, live markup.
    html = re.sub(r"<!--.*?-->", "", entry.read_text(encoding="utf-8"), flags=re.S)
    css = ""
    js = ""
    for css_file in (args.site_dir / "assets" / "css").glob("*.css") if (args.site_dir / "assets" / "css").exists() else []:
        css += css_file.read_text(encoding="utf-8") + "\n"
    for js_file in (args.site_dir / "assets" / "js").glob("*.js") if (args.site_dir / "assets" / "js").exists() else []:
        js += js_file.read_text(encoding="utf-8") + "\n"

    results = []
    check_html(html, results)
    check_seo(html, args.site_dir, results)
    check_css(css, results)
    check_contrast(css, results)
    check_copy(html, results)
    check_placeholders(html, js, results)

    fails = [r for r in results if r[0] == FAIL]
    warns = [r for r in results if r[0] == WARN]
    oks = [r for r in results if r[0] == OK]

    for level, cat, msg in results:
        print(f"[{level:4}] {cat:12} {msg}")

    print(f"\n{len(oks)} ok, {len(warns)} warnings, {len(fails)} failed")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
