# Stykka

**Vibe:** Scandi atelier under white light. Pure white canvas, hairline
black borders, zero accent color, zero shadow — the interface is
deliberately invisible so full-bleed photography carries every ounce of
warmth. Headlines whisper at weight 400, never shout at bold. Hierarchy
comes entirely from size, tracking and whitespace, not from color.

**Use for:** furniture, kitchens, interiors, craft goods, architecture,
photographers — anything with strong enough photography to be the entire
argument, and confident enough to need no accent color to sell it.

**Avoid for:** anything without at least one genuinely strong, editorial
photograph per section - this system has nowhere to hide a weak image.
Also avoid where secondary/muted text hierarchy matters: Stykka uses one
ink value for all text, by design (see Notes) - a site that leans on
grey-for-less-important won't have that lever here.

**Signature move (not a default, the point of the system):** display
headlines set at weight **400**, never 500+, at aggressive negative
tracking (-1.2px to -1.93px) so they read architectural rather than
typeset. Buttons are outlined-only, 1px black border, transparent fill,
inverting to solid black on hover - the only button geometry in the
system.

**Suggested pairing (starting point, not a default):** Inter / Inter -
one family for both headings and body, weight doing the work. Azeret Mono
reserved for a single editorial accent line, never a UI-wide mono/label
face.

```css
:root {
  --ink:        #000000;
  --ink-soft:   var(--ink); /* deliberate: source system uses one ink value
                                for every text element, never a second tone -
                                "never introduce a second ink color" is one
                                of its own explicit rules */
  --ground:     #ffffff;
  --raised:     var(--ground); /* no distinct surface fill - structure comes
                                   from a 1px hairline border, not a tonal
                                   shift; "adding a drop-shadow breaks the
                                   editorial flatness" per source */
  --line:       #000000; /* full-strength, not a soft tint like every other
                             system here - the hairline IS the structure */
  --accent:     #000000; /* the system is achromatic by design - black
                             itself is the only "action" colour, via the
                             outlined-button-inverts-on-hover mechanism */
  --accent-lt:  var(--ground);
  --accent-ink: var(--ink);

  --display: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
  --body:    "Inter", -apple-system, BlinkMacSystemFont, sans-serif;

  --container: 1280px;
  --radius:    16px;  /* text-bearing surfaces (cards) */
  --radius-sm: 8px;   /* tags, buttons */
  --ease:      cubic-bezier(0.22, 1, 0.36, 1); /* source specifies no motion
                                                   at all - studio baseline
                                                   used, not invented */
  --section-y: clamp(3.75rem, 8vw, 5rem); /* tighter than every other system
                                              here - 60-80px section gaps in
                                              source, compact by design */
}
```

**Notes**

- Images are always **0px radius**, hard-edged to the grid line - never the
  16px card radius. The 16px is reserved for text-bearing surfaces only.
  This distinction matters and is easy to lose when adapting a pattern.
- Muted/secondary text has one real lever in the source system: `Plate Gray
  #b8b8b8`, but it's only safe on a black ground (10.6:1) - on white it's
  2.0:1, below the accessibility floor. Not carried into the token block
  for that reason; if a muted tone is genuinely needed on the white canvas,
  derive one that actually passes 4.5:1 rather than reaching for this value.
- Small-caps tracked uppercase labels (14px, +0.29px tracking) are the
  system's one repeated piece of chrome - every section opener uses one.
  Worth treating as load-bearing, not decorative, when adapting a pattern.
- Azeret Mono appears **at most once per page** in the source system - a
  single 18px editorial line breaking the Inter rhythm deliberately. Not a
  mono/label face used throughout, unlike how mono accents work in the
  other systems here (compare Espresso & Gold's Roboto Mono stat tags,
  used liberally). Respect that restraint when adapting.
- Element gaps are compact (10px) even though section gaps are generous
  (60-80px) - the compact density inside a section is what makes the
  whitespace *between* sections read as intentional rather than empty.

**Source:** https://styles.refero.design/style/b43fdb3c-85e9-4282-9262-1d3deb4b679d
(Stykka, via Refero). Extracted from a full token export the user provided
directly - not independently fetched, `styles.refero.design` is blocked by
this session's sandbox network egress.

*Added 2026-08-29.*
