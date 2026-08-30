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

**T14 - Full-bleed imagery is right; overlaid content still aligns to the
site's own container.** (2026-08-30)
T7 said "use the whole viewport" and that's correct - a section's image
should fill it edge to edge. What went wrong on the first pass: the hero's
*text* was given its own raw gutter padding instead of the site's shared
--container width, so it landed at a different left edge than the logo and
nav sitting directly above it - "text outside the margins." That
misalignment, not the full-bleed image itself, is what read as broken. Full
immersion and consistent alignment aren't in tension - an image can bleed
to the true edge while every piece of text on the page still shares one
left edge, always.

**T15 - Overlay the image, don't put text beside a framed one.** (2026-08-30)
A "text column + a photo in its own card" hero, even built cleanly with
real margins, reads like a generic template landing page - this was tried
directly and rejected. What the loved references actually do: the photo or
video fills the whole hero, and the text sits directly on top of it, graded
for contrast. Trust signals belong in that same frame too - a thin strip
pinned to the bottom of the image, not a separate bordered card living next
to the text, which reads disconnected and adds busyness rather than proof.
*From: cowboy.com, superpower.com, ag1.com. "Amble" was also named as a
reference in this round - not independently inspected (no screenshot or
fetch), noted here without a specific visual claim.*

**T16 - A headline earns short, elegant line breaks, not many forced short
ones.** (2026-08-30)
A long, multi-clause headline crammed into a narrow column wraps into four
or five choppy lines and reads heavy, not elegant. Split the idea across
the headline and the lede instead - a short, confident headline (two lines,
not four or five), with the qualifying clause moved down into the lede.

**T17 - The site's own deeper accent reads more considered than a bright
brand-utility colour on every button.** (2026-08-30)
A saturated action colour paired with a colour-matched glow on hover (e.g.
WhatsApp's own bright green, with a green-tinted shadow) is a common,
generic "sign up now" SaaS button pattern. Prefer the site's own deeper
accent for primary buttons site-wide; reserve the brighter brand-utility
colour for one clearly recognisable touchpoint where recognition genuinely
matters more than restraint (e.g. the floating WhatsApp icon). On a photo
or video background specifically, a plain white or near-white pill reads
cleaner than any coloured button - true in every reference this round.
*From: cowboy.com, superpower.com, ag1.com, anthropic.com*

**T17 correction - bright brand-utility green is fine on plain ground; the
glow shadow was the actual tell, not the hue.** (2026-08-30)
T17 above prescribed the site's deeper accent for primary buttons
site-wide. Overcorrected: on a follow-up, a concrete reference mock-up
(provided directly, not a general site) used the bright WhatsApp green with
a WhatsApp icon inside the button, on plain ground, and it was pointed to
as the wanted direction. Reverted to bright green + icon for every
WhatsApp-action button (nav, hero, final CTA) - the icon ties the colour to
the specific channel it names, same logic T17 already granted AG1's
"Shop Now." What still holds from T17: no colour-matched glow shadow on
hover (flat, a small lift only), and a white pill specifically for a button
sitting directly on a photo/video background. The real lesson: judge a
button by hue *and* context together, not hue alone - and when a concrete
mock-up is provided, it settles the question over a general principle.

**T18 - A hero can bleed its image to the true edge and still stay
container-aligned - the two aren't in tension.** (2026-08-30)
The reliable technique, arrived at after the T14 misalignment: let
`.hero__grid` span the full viewport width (not capped at `--container`) so
the image column can reach the real right edge, but give the text column's
own left padding a calculated value -
`max(var(--gutter), calc((100vw - var(--container)) / 2 + var(--gutter)))`
- so it lands at exactly the same x-position `.container`'s content does
at any viewport width. A diagonal cut on the image's inner edge (a
`clip-path` polygon, a few percent inset at the top, flush at the bottom)
reads as a considered, editorial detail rather than a plain rectangle or
card - came from a concrete reference mock-up, not a photo library.

**T19 - Don't vertically centre a short text block inside a tall
image-driven row.** (2026-08-30)
Centering a hero's text block inside a row whose height is set by the
image next to it (rather than by the text's own content) creates large,
equal gaps above and below the text - exactly the "dead space" complaint
this was meant to fix. Top-align the text column instead, with a fixed top
padding tuned to sit close under the header - let the image simply run
taller than the text below it, which reads as intentional, not empty.

**Resolving T15 vs. T18/T19.** T15 said "overlay the image, don't put text
beside a framed one" - built, and rejected in favour of the diagonal
text-beside-image split captured in T18/T19. Both stay recorded rather than
deleting T15, per the append-only rule, but T15 is *not* the standing
guidance for a hero layout - T18/T19 is, confirmed by a concrete mock-up.
T15's actual point still holds for a different case: a dedicated full-bleed
video/image *statement* moment (VIDEO-02 in the Pattern Library) - there,
overlaying the image with a localised scrim is still correct, because that
pattern's whole job is to be the image, not a supporting element next to
text. Read T15 as "true for a full-bleed statement section," not "true for
every hero."

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

**superpower.com** (2026-08-30)
Full-bleed portrait, warm circular glow isolating the subject from
whatever's actually behind them - a real technique for calming a busy or
plain background without losing the person. White pill CTA plus a
translucent dark-outline secondary, both sitting directly on the image. A
bottom trust strip (whole-body check / accessible / trusted), same pattern
as Cowboy's.

**ag1.com** (2026-08-30)
Full-bleed video hero, headline and one line of support overlaid directly
on it - bright brand-green primary CTA ("Shop Now") *does* work here, next
to a white-outline secondary, so a saturated accent isn't wrong on
principle - it read right on AG1 because the rest of the page is
restrained enough to earn it (see T2). Everything above the fold in one
uninterrupted composition.

**anthropic.com** (2026-08-30)
A different valid pattern from the other three here: headline and support
text first, on a plain ground, a video or image sits *below* rather than
behind the text. Solid black CTA, no colour. Referenced as an alternative
approach for a future project that wants text-first rather than image-first
- not what was chosen for Isaías's hero, but worth remembering as a second
option.

**amble** (2026-08-30)
Referenced by name alongside Cowboy - not independently inspected in this
session (no screenshot or fetch), so noted here without a specific visual
claim.

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
