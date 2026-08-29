---
name: website-studio
description: Design and build small-business websites end to end - from a Google Drive project folder to a finished static site, with a fast draft mode and scripted preview/QA checks. Runs a five-phase flow (brief, design direction, blueprint, build, QA) using a personal design-system library, a taste profile and global design guidelines. Use when starting a new client website, continuing an existing one, adding a design system to the library, or capturing a design preference. Triggers on "new site for", "client website", "build a website", "website studio", "add a design system", plus any request to design, restructure or polish a small-business site.
---

# Website Studio

A studio in a folder. It turns a Google Drive project folder into a finished
small-business website that looks designed, not generated.

## Operating principles

1. **The Drive folder is the source of truth.** Never invent a fact about a
   business. No price, claim, credential, testimonial or statistic goes on a
   site unless it came from the briefing, the client's own channels, or the
   client's mouth. If something is needed and missing, ask - or mark it
   clearly as a placeholder in both the HTML and the README.
2. **Decide, then show.** Make the design call, present it with one line of
   reasoning, let it be vetoed. Do not hand over menus of options for
   decisions you can make well.
3. **Every gate is skippable.** "skip" moves to the next phase on defaults.
   "just build it" runs everything to phase 4 with no stops. See **Draft
   mode** below for the explicit fast path.
4. **Capture taste silently.** See "Learning" below. Never interrupt the work
   to ask about the taste profile.

## Read before working

Always: `taste.md`, `guidelines.md`.
Phase 2 only: `STUDIO-LIBRARY.md`, `design-systems/*`, `resources.md`.
Phase 3/4, or any section request: `PATTERN-LIBRARY.md`, `snippets/motion.md`.
Phase 5 only: `qa.md`.
Do not load `qa.md` early - it is a checklist for finished work.

`scripts/preview.py` and `scripts/check.py` are tools, not reading - run
them, don't read them into context. See Phase 4/5 for when.

## Output format

Static HTML, CSS and JS. No build step, no framework, no CSS utility library.

- `index.html` - all markup, one `<section id="">` per block
- `assets/css/style.css` - `:root` token block at the top, then layout
- `assets/js/main.js` - menu, scroll reveal, any interaction
- `assets/img/` - optimised images, `.webp` where possible
- `README.md` - what is placeholder, what needs the client, how to publish

Rationale: swapping a design system must be a ~30-line token edit, not a
markup rewrite. Utility classes make that impossible and make every site look
the same. Custom CSS with tokens is the whole point.

**Exception:** if the client needs to edit their own copy after launch, stop
and say so - that is a Framer/Webflow job. Deliver a design spec (tokens,
structure, copy, shot list) instead of code.

## Draft mode

Triggered by "quickly", "just build it", "give me something to react to", or
similar. An explicit, repeatable path - not an improvised skip.

1. Run phase 0 and enough of phase 1 to have real facts - no invented
   content, that rule never lifts.
2. Make the phase 2 direction call yourself (system, fonts, photo plan) and
   state it in one line each as you build, instead of gating on approval.
3. Fold phase 3 into phase 4 - write real section copy directly into the
   markup as you build it, skipping the separate copy-approval gate.
4. Build. Run `scripts/preview.py <site_dir> <out_file>` and send the result
   - do not hand-roll an inline preview file again.
5. Present the whole thing as a draft to react to. Corrections here are
   taste signals like any other - log them per **Learning**.

Phase 5 (QA) is never skipped by draft mode - it happens once the direction
is confirmed, not before.

## The flow

### Phase 0 - Locate

**First, close the loop on the last project.** Check the working directory
(and its parent, if this is a fresh checkout) for a `.website-studio-learnings.md`
that was never consolidated into `taste.md`, and check whether `taste.md`
has a non-empty `## Pending` section. If either is non-empty, show it and ask
what to keep before starting anything new - taste signals that never get
reviewed are wasted work.

Then ask for the Google Drive project folder, or find it by business name
with `search_files`. Read everything in it: briefing doc, notes, logos,
photos, brand guidelines. List what is there and what is missing before
continuing.

**The briefing may not match `templates/briefing.md`.** Real client
documents are often a free-form doc, not the reusable template - extract the
same facts regardless of structure, don't require the template's shape.

### Phase 1 - Brief

Goal: a filled briefing with the fewest possible questions asked.

1. Read the project's Business Briefing doc in Drive. The reusable template
   lives at docs.google.com/document/d/1uEQMykt9Nne2jWWxtu7jpnxCHec5ra4rQyr8x_y6H3g
   (structure mirrored in `templates/briefing.md`).
2. Fill everything you can yourself, from: the client's current site, Google
   Maps listing (hours, address, review count and themes), Instagram, any
   notes or PDFs in the folder. Use WebFetch.
3. **Then ask only what actually changes the website.** Usually 3-5 questions.
   Never ask what you could have looked up. Prioritise: what the business most
   wants to grow, what the visitor should do, what makes them different, and
   anything a claim on the site would depend on.
4. Ask the language question here, because it changes the markup:
   **one language or two?** Default pt-PT. If bilingual, see
   `guidelines.md` - two HTML files, not a JS toggle.
5. Write the answers back into the Drive briefing doc so the folder stays the
   source of truth.

**Gate:** show the filled brief, flag every gap and assumption.

### Phase 2 - Direction

**Before anything else: "Do you want to check your Studio Library first?"**
If yes, open `studio-library.html` (see **The visual library** below) so the
saved design systems, fonts and animations can actually be seen - live
colours, real font rendering, working animation demos - not read as a
markdown list. If no, go straight to the routes below. Either way, ask once
per project, not once per sub-decision.

Two decisions, presented together.

**a) Design system.** Offer three routes, in this order:
- pick from `design-systems/` (list them with their one-line vibe notes -
  cross-reference `STUDIO-LIBRARY.md` if it was just shown)
- give a reference (a URL, a screenshot, or something browsed via
  **Inspiration flow** below) - derive a new system from it per
  `design-systems/_adding.md`
- ask for a recommendation - choose based on the business, say why in one line

None of these feel right? That's what **Inspiration flow** below is for -
don't stall here waiting for a reference that doesn't exist yet.

Then tune: fonts, palette, spacing, radii, motion. Fonts are chosen fresh per
project - a system's suggested pairing is a starting point, never a default.
Two sites from this studio must never twin.

**b) Photo audit.** The single biggest driver of whether a small-business site
reads as credible or cheap. Inventory what the client actually has, name the
3-5 shots that would carry the site, and produce a phone-shootable shot list
from `templates/shot-list.md`. Anything that cannot be shot: generate with
Higgsfield (see `resources.md`), or cut the section. Never ship a weak photo
big.

**Gate:** design system + token block + shot list.

### Phase 3 - Blueprint

The site structure **with real copy written in**. Never lorem, never
"[headline here]". Section by section: what it is, why it exists, the actual
headline, the actual body text, the actual call to action.

Copy rules are in `guidelines.md` - the short version: second person, concrete,
specific to this business, no premium filler.

**Gate:** the client-facing text is the thing being approved here. Expect
edits and take them literally - a rewritten headline is a taste signal.

### Phase 4 - Build

Write the site. Order: tokens, base, layout, sections top to bottom, then JS.

For motion, start from `snippets/motion.md` rather than writing animation
from scratch - working code already tuned to the timing rules in
`guidelines.md`, not prose to reimplement each time.

Non-negotiables, enforced while writing, not after:
`prefers-reduced-motion`, `:focus-visible` on every interactive element,
semantic landmarks, real `alt` text, `clamp()` for fluid type and spacing,
`<title>` and `<meta name="description">`, Open Graph tags, favicon.

To hand over a preview, run:
`python3 scripts/preview.py <site_dir> <out_file> --mode full` for
SendUserFile, or `--mode artifact --title "..."` for the Artifact tool. Don't
hand-write the inlining again.

### Phase 5 - QA

Run `python3 scripts/check.py <site_dir>` first - it catches contrast
failures, missing alt text, broken anchors, missing meta tags, banned vague
copy phrases and leftover placeholders faster than reading for them. Fix
what it flags, then load `qa.md` for the parts a script can't see: real
responsive widths, motion in an actual browser, and the honest "does this
look generated" read in section 10. Then present the taste captured this
project (see below) and ask whether to keep it.

## Learning

Throughout every project, watch for taste signals and log them silently to
`.website-studio-learnings.md` in the project working directory:

- a design decision rejected or reversed
- the same correction made more than once
- a headline rewritten - note what changed about the voice
- a strong reaction to a reference

At the phase 5 gate, present them as a short list and ask what to keep.
Approved entries are appended to `taste.md` with today's date - **append only,
never rewrite existing entries.**

**Project fact vs. principle.** "The gold should be warmer" on one site is a
project decision - it does not belong in `taste.md`. "I always want warmer
accents than you pick" is a principle - it does. When unsure, file it under
`## Pending` in `taste.md` and raise it at the next consolidation.

Consolidation happens only when asked: merge duplicates, resolve pending
entries, and show a diff before changing anything.

## The visual library

`STUDIO-LIBRARY.md` is the source of truth - always edit it first. But never
show it as the markdown file. `studio-library.html` is the browsable version:
live colour swatches and mini mockups rendered from each design system's real
tokens (not screenshots - three of the five systems have never shipped a real
site to screenshot), actual Google-Fonts-rendered type samples for the saved
pairings, and working demos for every animation (a replay button for the two
that need one, a real hover state, real clickable tabs, a running marquee).

**"Show me the Studio Library"** - or the phase 2 library-check question
answered yes - means: open `studio-library.html` (SendUserFile, `display:
render`), not print the markdown.

**Keeping the two in sync.** `studio-library.html` is hand-built to match
`STUDIO-LIBRARY.md`, not generated by a script - the content is genuinely
bespoke (each design system needs its own real colours and font stack in its
card, each font pairing needs a real sample line, each animation needs a
working demo), which doesn't reduce to a template. Whenever `save to
library`, `add-system` or `add-resource` adds an entry to
`STUDIO-LIBRARY.md`, add a matching card to `studio-library.html` in the same
turn, following the pattern of the existing cards for that section. Don't let
them drift - if asked to show the library and the HTML is behind, update it
first.

## Inspiration flow

For when the library doesn't have what's needed - a whole direction, or just
one section pattern (a hero, a pricing layout, a nav interaction). Reachable
any time, not only at phase 2 - "I need inspiration" or "give me options for
X" both trigger it directly, without waiting for the phase 2 gate.

1. **Check the Studio Library first.** Open `studio-library.html`, always -
   see **The visual library** above. Never skip straight to external sources.
2. **If more options are wanted,** browse `resources.md`'s "Inspiration
   browsing" list - matched to what's needed: Refero for a whole direction,
   Land-book or One Page Love for a section pattern or page flow, SaaSFrame
   for a conversion/marketing section, Mobbin for an interaction, Fontesk for
   a font. Fetch one or two specific references worth reacting to - don't
   dump a whole site's catalogue into the conversation.
3. **Let the choice happen.** Present what was found, wait for a pick. Don't
   pre-select - this step exists because the library alone wasn't enough,
   so the point is more real options, not a faster route back to one.
4. **Adapt, never import wholesale.** Translate the chosen pattern into the
   *project's own* design system - its tokens, its fonts, its accent - same
   "translate, don't copy" rule as `design-systems/_adding.md`. The pattern's
   structure and idea transfer; its literal colours and fonts don't. The
   result should feel like the rest of the site, not a borrowed section
   bolted on.
5. **Save only when asked.** A pattern used once for one project stays in
   that project. It enters `STUDIO-LIBRARY.md` only on an explicit
   `save to library` - never automatically, even for something that worked
   well and could clearly be reused.

## Pattern Library

`PATTERN-LIBRARY.md` holds reusable **section** patterns - layout,
hierarchy and interaction. Never final visual style. This is the structural
counterpart to the Studio Library (style layer: systems, fonts, animations) -
keep the two separate, that separation is the point. Categories: Heroes,
Testimonials / Comments, Services, Pricing, About, CTAs, FAQs, Galleries.
Empty categories are real gaps, not placeholders to fill with invented
patterns.

**The token contract.** A pattern's code in `patterns/*.html` consumes only
design-system tokens (`--ink`, `--ink-soft`, `--ground`, `--raised`,
`--line`, `--accent`, `--accent-lt`, `--accent-ink`, `--display`, `--body`,
`--radius`, `--radius-sm`, `--ease`, `--section-y`) - never a hardcoded
colour or font. Every design system in `design-systems/` guarantees this
exact set (aliased where its own naming differs - see the "pattern contract
aliases" comment in each file). This is what makes "adapt to the current
design system" close to free: swap which system's tokens are loaded, the
pattern doesn't change at all. When deriving a new design system (`add-system`
or the Inspiration flow), give it this same set or the pattern library won't
work with it.

**"Show me my patterns" / "browse the pattern library"** - open
`pattern-library.html` (SendUserFile, `display: render`), never print
`PATTERN-LIBRARY.md`. Every card renders the pattern's real code twice, in
two different saved design systems side by side, proving the same layout
survives a totally different look - not a static screenshot.

**Keeping the two in sync**, same rule as the Studio Library:
`pattern-library.html` is hand-built to match `PATTERN-LIBRARY.md`, not
generated by a script - genuinely bespoke content (each pattern's own real
markup, each with a working interactive demo). Whenever a pattern is saved,
add a matching card in the same turn.

### Default flow for a section request

Triggered by something like "add a testimonial section" - a request for one
section, not a whole project phase.

1. **Choose a suitable pattern from `PATTERN-LIBRARY.md` by default.** Decide
   based on the category and what fits the business and the content
   available (e.g. many short quotes -> a marquee pattern; a few strong ones
   -> a rotating-quote pattern). Don't ask which - per **Decide, then show**.
2. **Adapt it to the current design system** - the token contract above.
3. **Build it** - write it into the project's actual files.
4. **Give a preview link** - `scripts/preview.py`, same as any other build
   step.

**If it's not right,** offer exactly these three, in this order, and let the
pick happen without pre-selecting:

1. **Browse the Pattern Library** - open `pattern-library.html` so the saved
   options for this category can actually be seen and compared.
2. **Find inspiration** - re-surface the relevant entries from
   `resources.md`'s "Inspiration browsing" list (see **Inspiration flow**
   above) - a reminder of where to look, not a re-run of the whole flow from
   scratch.
3. **Create something new** - design a pattern from scratch for this
   project, same token-only discipline as everything else in the library.

**If something new gets built and genuinely liked,** ask whether to save it
as a reusable pattern. Only on yes: assign the next ID in that category,
write it to `patterns/`, add an entry to `PATTERN-LIBRARY.md` and a card to
`pattern-library.html` in the same turn.

## Side modes

Invoked any time, mid-project or standalone:

- **learn** - "remember that I..." / "never do X again" -> append to `taste.md`
- **add-system** - a reference URL or screenshot -> new `design-systems/*.md`
  per `_adding.md`, plus an entry in `STUDIO-LIBRARY.md`
- **add-resource** - a useful link -> `resources.md`, with one line on when to
  reach for it
- **save to library** - a design system, font pairing or animation worth
  keeping -> append one entry to the relevant `STUDIO-LIBRARY.md` section,
  in its existing format (Name/ID, reference, what's liked, best use cases).
  Append only, same as `taste.md` - never reorder or delete existing entries.
- **save as a pattern** - a section built from scratch worth reusing -> next
  ID in its category, code to `patterns/`, entry in `PATTERN-LIBRARY.md`,
  card in `pattern-library.html`. Same append-only rule. Never automatic -
  see **Pattern Library** above.
