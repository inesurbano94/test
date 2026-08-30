# Design taste

Append-only. New entries go at the bottom of their section with a date.
Never rewrite an existing entry - if taste changes, add the correction and
note that it supersedes.

Established 2026-08-28 from an interview plus the Isaías Rocha site.

---

## Principles

**T1 - Credibility comes from people, not adjectives.** (2026-08-28)
Real humans carry a small-business site: customers giving feedback, the owner
mid-work, people in action. Faces do the persuading that copy claims to do.
A site with no people on it has to work much harder to be believed.
*From: drinkag1.com*

**T2 - Simple frame, rich content.** (2026-08-28)
Generous white space, restrained palette, few type sizes - so that the
photography and the words carry the page. Simplicity is the container, not
the content. An empty-feeling minimal site has missed the point.
*From: airbnb.com, drinkag1.com*

**T3 - Copy speaks to "you", never about "us".** (2026-08-28)
Second person, direct, concrete. The visitor should feel addressed, not
marketed at. This applies to headlines hardest.
*From: tonyrobbins.com, airbnb.com*

**T4 - Motion is a sign of life, not decoration.** (2026-08-28)
Small looping video, subtle reveals on scroll, considered hover states. Motion
earns its place by making the page feel alive or by clarifying a relationship.
Never motion for its own sake, and never in an already busy layout.
*From: tonyrobbins.com*

**T5 - One accent on a near-neutral base.** (2026-08-28)
Warm neutrals preferred over cold grey. A single accent colour doing all the
work of emphasis beats a palette of competing colours.
*From: the Isaías site - cream/paper grounds, espresso ink, one gold accent*

**T6 - Structure over symmetry.** (2026-08-28)
Three-card grids are fine and often right - AG1 uses them well. What is not
fine is *everything* being in threes with no hierarchy. Some things on a page
matter more than others and the layout should say so.

**T7 - Use the whole viewport, not a boxed container.** (2026-08-30)
Generous container widths and edge-to-edge imagery over a narrow centered
column with wide empty gutters on either side. Editorial and immersive, not
brochure-in-a-frame. Applies to every section, not just the hero - a wider
container is a site-wide setting, not a hero-only trick.
*From: cowboy.com, rhode (rhodeskin.com), tonyrobbins.com*

**T8 - Distinctive display type over safe neutral grotesques.** (2026-08-30)
A title font is allowed to look chosen, not defaulted to. When picking from
the Font Library, weigh how curated a pairing reads, not just how clean or
safe it is - a font with real character over one that could belong to any
site.

**T9 - Consistent heading hierarchy, site-wide.** (2026-08-30)
Every section title (h2) shares one size; every card or sub-heading (h3)
shares another - set once, globally, never scoped per-section by accident.
Inconsistent heading sizes read as unfinished even when each one looks fine
in isolation.

**T10 - Copy is edited down, hard.** (2026-08-30)
A strong headline, one short supporting line, then let imagery and
hierarchy carry the rest. Large paragraphs are the tell to watch for -
strongest to enforce in heroes and About sections specifically, the two
places most tempted to over-explain.

**T11 - Overlay text with a localised scrim, not a flat wash.** (2026-08-30)
When text sits on a photo or video, darken only the pocket directly behind
the text (a soft radial scrim) and leave the rest of the image clear - reads
as photographic grading, not a UI layer laid over the whole frame. A flat
linear gradient wash across an entire image is a generic-template tell.
*From: cowboy.com*

**T12 - A hero is a complete composition, not a preview of one.** (2026-08-30)
Everything that makes the hero's point - headline, one line of support,
action, key proof - visible together on load, with real imagery doing real
work (full-bleed, a split image/text treatment, or another image-led
composition). Never a hero that needs scrolling to feel finished.
*From: cowboy.com, tonyrobbins.com*

**T13 - Lean image-rich, generously.** (2026-08-30)
Prefer more real photography over more text. When a client's own
photography is thin, say so plainly and use tasteful stock or a clearly
marked placeholder rather than letting the design go image-light to match
what's on hand - it should still read as intended once real photos land.

---

## Website References

Whole sites loved, kept as direct creative inspiration - not distilled into
a principle here (see Principles above for that), the actual site itself.
Reach for these when designing something fresh: how they think about a
problem, never what to copy. Append only, same rule as everywhere else.

**drinkag1.com** (2026-08-28)
Credibility through people - customer feedback, people in action, everywhere.
Simple frame: white space, restrained palette, few type sizes, so the photos
and the words carry the page. Three-card grids used well - structured, not
just decorative.

**airbnb.com** (2026-08-28)
Simple, minimalist, yet the content stays genuinely engaging - simplicity as
the container, never the content itself. Copy always speaks to the visitor
directly, never about the company.

**tonyrobbins.com** (2026-08-28)
Motion used as a sign of life - small looping video, considered hover states
- not decoration. Copy speaks directly to the visitor even in a busier,
less minimal layout than the other two references here.

**cowboy.com** (2026-08-30)
Full-viewport imagery, minimal container framing - the product and the
person carry the page, not a boxed-in hero. A localised dark scrim sits
behind on-image text only, never a flat wash across the whole frame. The
bottom of the hero carries a trust strip (award/feature badges) directly on
the image with almost no scrim at all - confident enough not to need one.

**rhode (rhodeskin.com)** (2026-08-30)
Referenced by name, alongside Cowboy, for viewport usage and image-led
composition - not independently inspected in this session (no screenshot or
fetch), so noted here without a specific visual claim.

---

## Banned by default

Override per project only with a stated reason.

- **Purple/blue gradients and glow.** Violet-to-blue washes, glowing orbs,
  dark-mode-by-default tech aesthetic. The single clearest tell of a generated
  site. (2026-08-28)
- **Emoji as icons, and generic icon rows.** 🚀 ✨ 💡 as section markers, or
  three-column feature grids of meaningless outline icons. (2026-08-28)
- **Vague premium copy.** "Elevate your experience", "Where quality meets
  passion", "Your journey starts here". If the sentence would work for any
  other business, it is not copy, it is filler. (2026-08-28)

Inferred from the Isaías site, correct if wrong:
- Pure black on pure white - warm ink on warm paper instead
- Cold system greys as a palette
- Hard-cornered boxes everywhere - there is a consistent soft radius
- Bouncy or elastic easing - motion is expo-out and calm

---

## Working preferences

- **Static HTML/CSS/JS, no build step.** Tokens in `:root`, hand-written CSS.
  No Tailwind or utility frameworks. (2026-08-28)
- **Fonts are chosen fresh every project.** No house pairing. Fraunces + Inter
  was right for Isaías, not a default. Two sites must never twin. (2026-08-28)
- **Claude drafts all copy, Inés edits.** Draft in full, never leave
  placeholders for the client-facing text. (2026-08-28)
- **Projects are usually pt-PT, often bilingual pt-PT + EN.** (2026-08-28)
- **Decide, then show.** Present the call with reasoning, not a menu of
  options. (2026-08-28)

---

## Pending

Signals not yet confirmed as principles. Raise at the next consolidation.

*(empty)*
