# Adding a design system

Triggered by the `add-system` mode, or by phase 2 when a reference is given
instead of a library pick.

## From a reference (URL, screenshot, or refero page)

1. **Read the tokens, not the vibe.** Fetch the page and extract the actual
   values: font families and weights, the type scale, the palette with hex
   values, spacing rhythm, border radii, transition durations and easing.
   `WebFetch` the CSS where possible; read carefully from a screenshot where
   not.
2. **Name what makes it work** in two or three sentences. Not "modern and
   clean" - what specifically: the contrast between a heavy display face and
   thin body, the single accent used only twice per screen, the unusually
   generous section padding. This is the part that transfers.
3. **Translate, do not copy.** Take the structural decisions, not the brand.
   Never lift a palette wholesale from a real company's site onto a client's.
4. **Write the file** with the same shape as the existing systems: vibe, use
   for, avoid for, suggested pairing, token block, notes.
5. **Test it against the guidelines before saving.** Contrast ratios, minimum
   body size, motion durations. A system that violates `guidelines.md` gets
   fixed, not saved as-is.

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
