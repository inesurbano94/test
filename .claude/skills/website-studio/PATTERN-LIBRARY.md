# Pattern Library

Reusable **section** patterns — layout, hierarchy and interaction only.
Never final visual style. A pattern's code consumes the project's own
design-system tokens (`--ink`, `--accent`, `--display`, `--radius`, etc.) and
nothing else — no hardcoded colours or fonts — so dropping the same pattern
into two different projects produces two visually distinct sections that
still feel structurally right for both. See **Pattern Library** in SKILL.md
for the token contract every design system must expose for this to work.

This is the layout counterpart to `STUDIO-LIBRARY.md`, which holds the style
layer (design systems, fonts, animations). Keep them separate — that
separation is the point.

**Optional inspiration, not the default build method.** website-studio
designs every section fresh by default — the business, `taste.md`, the
Website References section of `taste.md`, the chosen design system, and
its own judgement. This library gets opened only when asked to browse
options, when a built section isn't working and alternatives are wanted,
or when asked for inspiration on one section by name. It exists to expand
what's possible, not to cap it. See **Default: design it, don't assemble
it** in SKILL.md.

**To browse:** ask "show me my patterns" or "browse the pattern library" any
time - opens `pattern-library.html`, never this markdown file.

**To add something new:** build a pattern from scratch for a project, and if
it's genuinely reusable and liked, say `save as a pattern` - see SKILL.md's
default flow. New entries go at the bottom of their category - nothing here
is ever reordered or deleted, only added to.

Format per entry: **ID + name · code file · description · source ·
best for.**

---

## Heroes

**H01 — Split Hero with Proof Panel**
- Code: `patterns/hero-split-proof.html`
- What it is: Heading/lede/actions on one side, a stat/proof card (3 rows)
  on the other. The proof panel is what makes this different from a plain
  hero — it puts credibility beside the pitch, not below the fold.
- Source: shipped on the Isaías rebuild.
- Best for: businesses with real numbers to lead with — certifications,
  response time, years, review counts. Needs at least 3 real ones.

## Testimonials / Comments

**T01 — Infinite Marquee**
- Code: `patterns/testimonials-marquee.html`
- What it is: Quote cards drift continuously, no pagination, pause on
  hover. Ambient, not interactive.
- Source: adapted from SaaSFrame's testimonial-marquee category and
  `snippets/motion.md` §4.
- Best for: many short quotes, none needing to dominate. The default pick
  when there are 4+ real testimonials of similar length.

**T02 — Single Rotating Quote**
- Code: `patterns/testimonials-rotating-quote.html`
- What it is: One quote at a time, prev/next arrows plus dot pagination.
  One focal point, fully interactive.
- Source: adapted from One Page Love's CROJungle feature, simplified
  (dropped the cursor-follow image panel).
- Best for: a handful of strong, longer quotes each worth reading in full
  rather than skimmed in motion.

## Services

*No patterns saved yet.*

## Pricing

**P01 — Tabbed Plan Grid**
- Code: `patterns/pricing-tabbed.html`
- What it is: Pill tabs switch between context groups (e.g. venue vs. home
  visit), each showing a card grid.
- Source: shipped on the Isaías rebuild.
- Best for: businesses with genuinely different pricing per context. For
  one flat price list, use a plain grid instead — tabs would be decoration
  with nothing to switch between.

## About

*No patterns saved yet.*

## CTAs

**C01 — Centered Final CTA**
- Code: `patterns/cta-centered.html`
- What it is: Centered eyebrow, heading, one line, a single primary action,
  on a tinted section.
- Source: shipped on the Isaías rebuild.
- Best for: the last section before the footer. Deliberately one action,
  not two — don't split attention this late in the page.

## FAQs

**F01 — Accordion (single-open)**
- Code: `patterns/faq-accordion.html`
- What it is: One question open at a time; opening a new one closes the
  last. Icon rotates 45° to become a close mark.
- Source: shipped on the Isaías rebuild.
- Best for: almost any FAQ section. Open the question visitors ask most by
  default, not the first one alphabetically.

## Galleries

*No patterns saved yet.*

## Video Sections

**VIDEO-01 — Contained Video Statement**
- Code: `patterns/video-contained-statement.html`
- Reference: `patterns/references/video-01-programa-desktop.webp`,
  `patterns/references/video-01-programa-mobile.webp`
- What it is: A short video, contained within the page with margins and
  rounded corners (not full-bleed), with a strong text statement overlaid.
  Reads as a considered, framed moment rather than a hero takeover.
- Source: programa.design
- Best for: a business that wants one video moment to feel deliberate and
  contained — a quote, a proof statement, a single feature — without it
  dominating the whole viewport.
- First real use: Isaías rebuild (2026-08-29) — no video footage existed
  yet, so it shipped with the real hero photo as a poster-frame placeholder,
  clearly marked in the HTML and README. Swap for real footage per the
  shot list; the section doesn't change otherwise.

**VIDEO-02 — Full-Bleed Video Statement**
- Code: *none yet — build on first real use, per the reference note below.*
- Reference: `patterns/references/video-02-tonyrobbins-desktop.webp`,
  `patterns/references/video-02-tonyrobbins-mobile.webp`
- What it is: A short video filling the available width, edge to edge, with
  large centered text and an optional CTA overlaid directly on it.
- Source: tonyrobbins.com
- Best for: a hero-level moment — the video *is* the section, not a frame
  around it. Needs footage strong enough to carry that much visual weight.

**Reference-only note (VIDEO-02).** Still a structural reference, not built
yet - per the Pattern Library's own rule, code gets written the first time a
project actually uses it, not speculatively now. When that happens: adapt
typography, colour, spacing, radius, buttons and motion to the active
project's tokens - same token contract as every other pattern, including
this reference's own margins and full-bleed choice, which are structural
(radius/spacing decisions), not literal borrowed style.

---

*Nothing above is invented — each entry either traces to shipped work or an
explicit inspiration source, restyled rather than copied. Keep it that way
when adding new entries.*
