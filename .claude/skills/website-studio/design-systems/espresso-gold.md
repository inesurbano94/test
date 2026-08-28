# Espresso & Gold

**Vibe:** Warm editorial. Cream paper, deep espresso ink, a single antique
gold accent. Serif headings with real character over a quiet sans. Calm,
crafted, a little expensive. Feels handmade rather than manufactured.

**Use for:** personal trainers, coaches, therapists, artisanal food, barbers,
independent restaurants, anything where the owner *is* the product.

**Avoid for:** tech, clinical or medical services, anything that needs to feel
fast, cheap or high-volume.

**Suggested pairing (starting point, not a default):** Fraunces / Inter.
Alternatives with the same feel: Instrument Serif / Söhne · Bodoni Moda /
Work Sans · Newsreader / Public Sans.

```css
:root {
  --ink:        #1c1712;
  --ink-soft:   #5c5347;
  --deep:       #1b140d;
  --deep-2:     #2a2015;
  --paper:      #fbf8f2;
  --cream:      #f6f1e6;
  --beige:      #efe6d4;
  --line:       rgba(28, 23, 18, 0.12);
  --accent:     #b6874a;
  --accent-lt:  #d9b783;
  --accent-soft:#e6d3ae;
  --accent-ink: #3b2a14;

  --display: "Fraunces", Georgia, serif;
  --body:    "Inter", -apple-system, BlinkMacSystemFont, sans-serif;

  --container: 1180px;
  --radius:    14px;
  --radius-sm: 8px;
  --ease:      cubic-bezier(0.22, 1, 0.36, 1);
  --section-y: clamp(4.5rem, 10vw, 8rem);
}
```

**Notes**
- Headings at weight 500, `line-height: 1.08`, `letter-spacing: -0.01em`.
- Eyebrow labels: sans, uppercase, 0.75rem, weight 600, `letter-spacing: 0.18em`.
- Gold is for emphasis only - one or two elements per screen. Gold everywhere
  reads as cheap, not luxurious.
- Dark sections use `--deep` full-bleed with `--cream` text; they work as
  punctuation between paper sections, roughly one per three.
- Photography: warm grade, shallow depth, natural light. Cold or flash-lit
  photos fight this system badly.

*Extracted from the Isaías Rocha site, 2026-08-28.*
