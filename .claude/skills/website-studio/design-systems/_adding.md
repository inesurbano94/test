# Adding a design system

Triggered by the `add-system` mode, or by phase 2 when a reference is given
instead of a library pick.

## From a reference (URL, screenshot, or refero page)

Triggered by "add this design system" plus a link (or screenshot). All four
of these happen, same turn:

1. **Read the tokens, not the vibe.** Fetch the page and extract the actual
   values: font families and weights, the type scale, the palette with hex
   values, spacing rhythm, border radii, transition durations and easing.
   `WebFetch` the CSS where possible; read carefully from a screenshot where
   not. **If the fetch is blocked or fails** (some inspiration sites are -
   this has happened before with Refero, SaaSFrame, One Page Love in a
   sandboxed session), say so plainly and ask for a screenshot instead of
   guessing at tokens or inventing plausible-looking hex values. Nothing in
   this library is invented - a missing token stays missing until it's real,
   it doesn't get filled in with a good guess.
2. **Name what makes it work** in two or three sentences. Not "modern and
   clean" - what specifically: the contrast between a heavy display face and
   thin body, the single accent used only twice per screen, the unusually
   generous section padding. This is the part that transfers.
3. **Translate, do not copy.** Take the structural decisions, not the brand.
   Never lift a palette wholesale from a real company's site onto a client's.
4. **Write the file** with the same shape as the existing systems: vibe, use
   for, avoid for, suggested pairing, token block, notes, and a **Source**
   line with the real URL - not just named in prose, an actual link, so it
   can be clicked back to and viewed later.
5. **Test it against the guidelines before saving.** Contrast ratios, minimum
   body size, motion durations. A system that violates `guidelines.md` gets
   fixed, not saved as-is.
6. **Add it to `STUDIO-LIBRARY.md` and `studio-library.html` in the same
   turn** - see **Show, don't tell** in SKILL.md. The gallery card's source
   link points at the same URL as the file's Source line.

## Using a saved system on a project

**Never modify the original.** Tuning a saved system's fonts, colours,
spacing, motion or imagery for a client happens entirely in *that project's*
own files (`assets/css/style.css`) - the file in `design-systems/` is never
edited to fit one client. If the tuning is good enough to want again, it
becomes a **new**, separately named entry (see `clinic-white.md` vs. the
Isaías rebuild's "Clinic White — tuned" in `STUDIO-LIBRARY.md`) - never an
overwrite of the original. The original stays a clean starting point for
every project after this one, including ones that want it untouched.

## From scratch, for a project

Same file shape. Build it from the business itself before any reference site:
the colours of the actual premises, the materials, the light. Write down where
each token came from - that provenance is what stops the next project reusing
it thoughtlessly.

## Rules

- One file per system, kebab-case filename, in this folder.
- The suggested pairing is always labelled as a starting point. Fonts are
  chosen fresh per project.
- Systems are starting points, not templates. Every project tunes the tokens.
- Note at the bottom where the system came from and the date.
