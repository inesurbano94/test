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
Phase 4 only: `snippets/motion.md`.
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
If yes, show `STUDIO-LIBRARY.md` in full - all three sections - so the
saved design systems, fonts and animations can be browsed before choosing or
adding anything new. If no, go straight to the routes below. Either way, ask
once per project, not once per sub-decision.

Two decisions, presented together.

**a) Design system.** Offer three routes, in this order:
- pick from `design-systems/` (list them with their one-line vibe notes -
  cross-reference `STUDIO-LIBRARY.md` if it was just shown)
- give a reference (a URL, a screenshot, or a styles.refero.design page) -
  derive a new system from it per `design-systems/_adding.md`
- ask for a recommendation - choose based on the business, say why in one line

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
