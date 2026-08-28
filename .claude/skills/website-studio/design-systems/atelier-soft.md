# Atelier Soft

**Vibe:** Quiet, tactile, unhurried. Muted off-whites with a colour cast,
low-contrast type, lots of air. Nothing shouts. Reads as considered and
personal - a studio, not a shop.

**Use for:** beauty and nails, yoga and pilates, ceramics and craft studios,
florists, interior designers, small clothing labels, therapists.

**Avoid for:** anything urgent, high-volume or price-competitive, and anything
needing loud calls to action - the register works against conversion pressure.

**Suggested pairing (starting point, not a default):** Reforma / Sligoil.
Alternatives: GT Sectra / Suisse Int'l · Ivy Presto / Neue Montreal ·
Cormorant / Jost.

```css
:root {
  --ink:        #35302b;
  --ink-soft:   #7b7269;
  --ground:     #f4f0ea;
  --ground-2:   #ebe4db;
  --raised:     #fbf9f6;
  --line:       rgba(53, 48, 43, 0.10);
  --accent:     #8f6f5a;
  --accent-lt:  #cbb3a1;
  --accent-soft:#e3d5c8;

  --display: "Reforma", Georgia, serif;
  --body:    "Sligoil", -apple-system, sans-serif;

  --container: 1080px;
  --radius:    2px;
  --radius-sm: 2px;
  --ease:      cubic-bezier(0.33, 1, 0.68, 1);
  --section-y: clamp(5.5rem, 12vw, 9.5rem);
}
```

**Notes**
- The most generous spacing of the four systems. Air is the design.
- Low contrast is deliberate but has a floor: body text still needs 4.5:1
  against its ground. Use `--ink`, not `--ink-soft`, for anything long.
- Nearly square corners, hairline rules instead of borders or shadows.
- Photography: natural light, muted, slightly desaturated, plenty of negative
  space in the frame itself. Busy or saturated photos break this system.
- Motion is very restrained - opacity and 8-12px rises, nothing more.
- Risk to watch: this system slides into "empty" easily. It needs real
  photography and real writing to hold the space it creates.
