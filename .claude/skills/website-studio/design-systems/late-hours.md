# Late Hours

**Vibe:** Dark, warm, high contrast. Near-black ground with warm undertone,
light type, one hot accent. Atmospheric rather than technical - lamplight, not
a dashboard. Photography does the heavy lifting and glows against the dark.

**Use for:** restaurants, wine bars, cocktail bars, tattoo studios, music
venues, nightlife, photographers, anything that happens in the evening.

**Avoid for:** daytime services, anything clinical or family-oriented, and any
business whose photos are bright and flat - they will look pasted on.

**Suggested pairing (starting point, not a default):** Editorial New / Söhne.
Alternatives: PP Right Grotesk / Inter · Canela / Neue Haas · Playfair
Display / Karla.

```css
:root {
  --ground:     #0d0b0a;
  --ground-2:   #171412;
  --raised:     #221d1a;
  --text:       #f2ece5;
  --text-soft:  #a49b91;
  --line:       rgba(242, 236, 229, 0.12);
  --accent:     #e0533a;
  --accent-lt:  #f28a72;
  --accent-ink: #2a0d07;

  --display: "Editorial New", Georgia, serif;
  --body:    "Söhne", -apple-system, sans-serif;

  --container: 1140px;
  --radius:    4px;
  --radius-sm: 2px;
  --ease:      cubic-bezier(0.22, 1, 0.36, 1);
  --section-y: clamp(5rem, 11vw, 9rem);
}
```

**Notes**
- Almost square corners - the softness comes from light and photography, not
  radii.
- Never pure black or pure white. The warm undertone in both is the system.
- Contrast is a real risk: `--text-soft` on `--ground-2` must be checked, and
  small text should use `--text`, not the soft variant.
- Images: darken slightly and warm the shadows so they sit in the ground
  rather than floating on it. Full-bleed works well here.
- Motion should be slower than usual - 450-500ms reveals. The register is
  unhurried.
- Menus, opening hours and booking must still be effortless to find. Atmosphere
  is not an excuse for hiding the practical information people came for.
