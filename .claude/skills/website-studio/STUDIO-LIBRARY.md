# Studio Library

Your saved visual references — browse this before choosing a direction on a
new project. This is an index: full detail (CSS tokens, working code) lives
in the files each entry points to. This file stays short on purpose.

**To browse:** ask "check my library" any time, or answer yes when asked at
the start of phase 2.

**To add something new:** say `save to library` with what you liked and why.
New entries go at the bottom of their section - nothing here is ever
reordered or deleted, only added to. Also reachable via the `add-system` and
`add-resource` side modes for the two most common cases.

Format per entry: **Name/ID · Reference · What I like · Best use cases.**
Design systems added from an external link also carry a **Source** line -
the real, clickable URL, so it can be opened and viewed directly, not just
named. Entries seeded before this existed (`Espresso & Gold`, `Clinic
White`, `Late Hours`, `Atelier Soft`) have no external source to link -
their `Origin` line says where they actually came from instead.

---

## Design Systems

**Espresso & Gold**
- Reference: `design-systems/espresso-gold.md`
- What I like: Warm editorial. Cream paper, deep espresso ink, one antique
  gold accent. Serif headings with real character over a quiet sans. Calm,
  crafted, feels handmade rather than manufactured.
- Best for: personal trainers, coaches, therapists, artisanal food, barbers,
  independent restaurants — anything where the owner *is* the product.
- Origin: extracted from the original Isaías Rocha site.

**Clinic White**
- Reference: `design-systems/clinic-white.md`
- What I like: Bright, clean, photo-forward. Trust built by evidence — faces,
  numbers, reviews, credentials — not adjectives. Modern commerce register,
  not minimalism for its own sake.
- Best for: health and wellness, nutrition, physio, supplements, anything
  sold on credibility and proof.
- Origin: seeded from the AG1 reference given during setup.

**Clinic White — tuned (Isaías rebuild)**
- Reference: `index.html` / `assets/css/style.css` on this branch, as
  rebuilt 2026-08-29.
- What I like: Proved the system can carry a project with weak photography —
  swapped the assumed photo-led proof for a type-and-data spine (the
  bioimpedance metrics did the credibility work instead of images). Fonts
  swapped fresh to Familjen Grotesk + Instrument Sans, palette shifted to a
  deep pine accent instead of the seed's green.
- Best for: proof-driven businesses with thin photo libraries — the variant
  to reach for first when a client has facts but not photos.

**Late Hours**
- Reference: `design-systems/late-hours.md`
- What I like: Dark, warm, atmospheric — lamplight, not a dashboard.
  Photography glows against the dark ground.
- Best for: restaurants, wine bars, cocktail bars, tattoo studios, music
  venues, nightlife — anything that happens in the evening.
- Not yet used on a real project — seeded from taste principles, unconfirmed.

**Atelier Soft**
- Reference: `design-systems/atelier-soft.md`
- What I like: Quiet, tactile, unhurried. Muted off-whites, low-contrast
  type, generous air. Reads as a studio, not a shop.
- Best for: beauty and nails, yoga and pilates, ceramics and craft studios,
  florists, interior designers.
- Not yet used on a real project — seeded from taste principles, unconfirmed.

**Stykka**
- Reference: `design-systems/stykka.md`
- Source: https://styles.refero.design/style/b43fdb3c-85e9-4282-9262-1d3deb4b679d
- What I like: Deliberately achromatic — no accent color at all, black
  hairlines and full-bleed photography doing all the work. Display
  headlines whisper at weight 400 instead of shouting at bold. Confident
  enough to need zero decoration.
- Best for: furniture, kitchens, interiors, craft goods, photographers —
  anything with strong enough photography to be the whole argument.
- Not yet used on a real project — added from a full token export the user
  provided directly (Refero was blocked by this session's network egress,
  so this wasn't independently fetched).

---

## Fonts

**Fraunces + Inter**
- Reference: used in Espresso & Gold, the original Isaías site.
- What I like: Editorial serif headings with real character, set against a
  quiet sans body that disappears and lets the serif carry the personality.
- Best for: warm, craft-led, personal-brand sites.

**Familjen Grotesk + Instrument Sans**
- Reference: used in the Isaías rebuild (Clinic White, tuned).
- What I like: Confident sans-only pairing — weight and size carry the
  hierarchy instead of a family switch. Reads modern and precise without
  going cold or corporate.
- Best for: proof- and data-led sites, health and wellness, anything that
  shouldn't feel handmade.

**Bricolage Grotesque + Inter + Roboto Mono**
- Reference: referenced from Say Briefly — not yet used on a real project.
- Roles: Bricolage Grotesque — headings/display. Inter — body. Roboto Mono —
  mono/accent (stats, labels, prices, anything numeric or code-like).
- Licence: both on Google Fonts, OFL 1.1 (Bricolage Grotesque, Inter) /
  Apache 2.0 (Roboto Mono) — free for commercial web use, confirmed.
- What I like: a three-tier system where the mono face does real work as an
  accent, not decoration — gives numbers and labels their own voice instead
  of borrowing the body font's.
- Best for: sites with real data to show off (prices, stats, specs) that
  want a grotesque-led, slightly technical feel without going cold.

**Inter + Azeret Mono**
- Reference: referenced from Stykka — not yet used on a real project.
- Roles: Inter — both headings and body, weight does the hierarchy work
  (600 for headings, 400 for body). Azeret Mono — mono/accent for labels,
  ids, small numeric details.
- Licence: both on Google Fonts, OFL 1.1 — free for commercial web use,
  confirmed.
- What I like: the calm of a single grotesque doing both jobs, with one
  quiet mono accent instead of a whole second display face. Minimal without
  being empty.
- Best for: quieter, precision-feeling sites — studios, tools, anything
  that shouldn't feel like it's trying hard.

---

## Animations

**Scroll Reveal**
- Reference: `snippets/motion.md` §1
- What I like: Fade plus a small rise, once, staggered across siblings.
  Motion as a sign of life, not decoration — matches taste principle T4.
  Used on the Isaías rebuild.
- Best for: section entrances, card grids. The default — almost every site
  should have at least this one.

**Orchestrated Hero Load-In**
- Reference: `snippets/motion.md` §5
- What I like: One considered moment on load instead of scattered effects —
  "spend your boldness in one place" applied to motion.
- Best for: once per site, hero only.

**Tab / Panel Switch**
- Reference: `snippets/motion.md` §3
- What I like: Content swap without a jump cut. Used on the Isaías pricing
  tabs.
- Best for: pricing comparisons, service switches, anywhere content changes
  in place.

**Magnetic Hover Lift**
- Reference: `snippets/motion.md` §2
- Best for: a single hero feature card or pricing card — not yet used on a
  real project.

**Marquee**
- Reference: `snippets/motion.md` §4
- Best for: certification badges, client logos, press mentions — not yet
  used on a real project, needs a real logo/cert list to justify it.

---

*Nothing above is invented for this list — each entry either traces to a
real project or is marked unconfirmed. Keep it that way when adding new
entries: say what you actually like about a reference, not what a template
would say.*
