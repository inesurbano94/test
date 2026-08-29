# Clinic White

**Vibe:** Bright, clean, photo-forward. Near-white ground, dense but ordered
information, one saturated accent. Trust built by evidence: faces, numbers,
reviews, credentials. The AG1 register - modern commerce, not minimalism for
its own sake.

**Use for:** health and wellness, dental and medical, nutrition, physio,
supplements and products, anything sold on credibility and proof.

**Avoid for:** businesses with weak photography - this system is mostly
photography, and it exposes bad images ruthlessly.

**Suggested pairing (starting point, not a default):** General Sans / Inter.
Alternatives: Satoshi / Satoshi (single family, two weights) · Untitled Sans /
Untitled Sans · Sora / Inter.

```css
:root {
  --ink:        #101418;
  --ink-soft:   #545c66;
  --ink-mute:   #8a939e;
  --white:      #ffffff;
  --off:        #f7f8f9;
  --tint:       #eef2f6;
  --line:       rgba(16, 20, 24, 0.10);
  --accent:     #1b6b4c;
  --accent-lt:  #d8ece2;
  --accent-ink: #0d3a29;
  --warn:       #c2410c;

  --display: "General Sans", -apple-system, sans-serif;
  --body:    "Inter", -apple-system, sans-serif;

  /* pattern contract aliases - see PATTERN-LIBRARY.md */
  --ground:  var(--off);
  --raised:  var(--white);

  --container: 1200px;
  --radius:    16px;
  --radius-sm: 10px;
  --ease:      cubic-bezier(0.22, 1, 0.36, 1);
  --section-y: clamp(4rem, 9vw, 7rem);
}
```

**Notes**
- Sans-only, and the hierarchy comes from size and weight, not family. Display
  weight 600, body 400. Nothing in between.
- Headings tight: `letter-spacing: -0.02em`, `line-height: 1.1`.
- The accent is a real colour, not a grey - swap the green for whatever the
  business owns. Keep the saturation; a desaturated accent kills this system.
- Proof elements are structural here, not decorations: review counts, star
  rows, credential badges, before/after, named testimonials with faces.
- Needs at least 6-8 strong photographs. If they do not exist, run the shot
  list first or pick a different system.
