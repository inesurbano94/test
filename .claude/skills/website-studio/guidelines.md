# Global website guidelines

Rules that hold across every project, whatever the design system. The design
system decides *which* fonts, colours and radii. These decide how they are
used.

---

## Typography

- **Two families maximum.** A display/heading face and a body face. A third is
  almost always a mistake.
- **Body text 17-19px** on desktop, never below 16px on mobile. Line height
  1.55-1.7 for body, 1.05-1.15 for large headings.
- **Fluid, not stepped:** `clamp(min, preferred-vw, max)` for headings and
  section padding. Set the min at the mobile size you actually want.
- **Measure 60-75 characters.** Long paragraphs at full container width are
  the most common readability failure. Cap with `max-width: 62ch`.
- **Negative tracking on large type** (`-0.01em` to `-0.03em`), positive on
  small uppercase labels (`0.12em` to `0.2em`).
- **Weights: pick two and commit.** Regular plus one emphasis weight. Heading
  faces often look best at 500, not 700.
- Self-host or preload webfonts; `font-display: swap`; subset to the
  characters the languages need (pt-PT needs ã õ ç á é í ó ú â ê ô à).

## Spacing

- **One scale, powers of a base.** e.g. 4 8 12 16 24 32 48 64 96 128. Every
  gap comes from the scale. Arbitrary values are how a layout loses rhythm.
- **Vertical section padding is the main dial for how expensive a site
  feels.** Generous. `clamp(4rem, 10vw, 8rem)` as a starting point.
- **Space belongs between related things, more between unrelated things.**
  If a heading is not visibly closer to its own paragraph than to the block
  above it, the hierarchy is broken.
- One container width for the whole site (1100-1200px typical), one padding
  rule, no exceptions without reason.

## Imagery

Per taste principle T1, this is the highest-leverage part of a small-business
site. See `templates/shot-list.md`.

- **People over objects. Action over posing.** A photo of the owner working
  beats a photo of the owner smiling at the camera.
- **Audit first, design second.** Know exactly what photos exist before
  designing sections that need them.
- **Never ship a weak photo large.** Options, in order: crop hard to the strong
  part; convert to a small supporting element; grade it toward the palette and
  overlay; cut the section. A bad hero image undoes everything else.
- **Grade toward the design system.** A consistent warm or cool cast across
  mismatched client photos makes them read as one set.
- Real `alt` text describing what is in the image. Decorative images get
  `alt=""`.
- `.webp`, sized to their actual display width, `loading="lazy"` below the
  fold, explicit `width`/`height` to stop layout shift.
- Stock photography is a last resort and usually a tell. AI imagery is
  acceptable for texture, backgrounds and things that cannot be photographed -
  not for fake customers or fake premises.

## Responsive

- **Design mobile first.** Most small-business traffic is a phone, often via
  Instagram or Maps.
- Breakpoints where the layout breaks, not at device names. Typically ~640,
  ~900, ~1200.
- **Test 360px wide.** Nothing overflows, nothing needs horizontal scroll.
- Tap targets 44px minimum. Phone numbers, WhatsApp and addresses are
  tap-to-act on mobile.
- Sticky elements must not eat a phone screen. One floating action button
  maximum.

## Motion

Per T4. Motion is life, not decoration.

- **Easing:** expo-out for entrances and movement -
  `cubic-bezier(0.22, 1, 0.36, 1)`. Never bouncy or elastic.
- **Duration:** 150-250ms for hover and state changes, 350-450ms for reveals
  and layout movement. Anything above 600ms feels broken.
- **Scroll reveal:** fade plus a small rise (12-20px), once, never repeating.
  Stagger siblings by 60-80ms. Never animate an entire section as one block.
- **Hover:** every interactive element has a state, and it is a *change of the
  same object*, not a different object appearing.
- **`prefers-reduced-motion: reduce` is mandatory** and written at the same
  time as the animation, not retrofitted.
- Never: parallax on text, auto-playing carousels, scroll-jacking, counters
  that count up, typewriter effects.

## Interactions

- Every interactive element: hover, focus-visible, and active states.
- `:focus-visible` outline in the accent colour with an offset. Never
  `outline: none` without a replacement.
- **The primary action is unmissable and repeated.** For small businesses this
  is usually WhatsApp, a phone call, a booking link or directions. Present in
  the hero, again mid-page, again in the footer.
- **One number, one link, one source.** Define the WhatsApp number, phone and
  booking URL once in JS or as a token, and read from it everywhere.
- Forms: real labels, `type` and `inputmode` set correctly, visible error
  text, no placeholder-as-label.
- Smooth scroll for anchors, with `scroll-margin-top` matching the sticky
  header so headings don't hide under it.

## Copy

Claude drafts, Inés edits. Per T3.

- **Second person.** "You" is the subject. The business is what makes the
  thing possible.
- **Specific beats impressive.** "Trains 40 people a week in Alvalade" beats
  "excellence in personal training".
- **Headlines say something.** If the headline could sit on a competitor's
  site unchanged, rewrite it.
- **Every claim traces to the briefing.** No invented statistics, testimonials,
  years-in-business or credentials. Placeholder testimonials, if explicitly
  requested to preview a layout, are marked in the HTML *and* the README.
- Lead with what the visitor gets, follow with what it costs them.
- Prices in full, honestly, if the client will allow it. Hidden prices are a
  conversion problem on small-business sites.
- pt-PT, not pt-BR: "casa de banho" not "banheiro", "telemóvel" not "celular",
  second person "tu" or "você" chosen deliberately and kept consistent.

## Bilingual sites

Decided at the brief gate because it changes the markup.

- **Two HTML files, not a JS toggle.** `index.html` (primary language) and
  `/en/index.html`. Shared CSS and JS.
- Rationale: a JS toggle hurts SEO, flashes the wrong language on load, and
  breaks with JS disabled. Local search visibility matters more to a small
  business than the maintenance saving.
- `<html lang="">` set per file, `<link rel="alternate" hreflang="">` in both,
  each pointing at the other and at itself.
- The language switcher links to the equivalent page, never to the homepage.
- Translate the meta description, OG tags and image alt text too.

## SEO

Small-business SEO is almost entirely local intent - "personal trainer
Alvalade", not a content strategy this studio doesn't run. Build for that.

- **Title formula:** `{Business} — {what they do} em {location} | {one
  differentiator}`. The words someone actually searches, not a slogan.
- **Meta description:** one clause on what the business does, one on why
  this one - the differentiator - always including the location. 150-160
  characters.
- **Heading hierarchy is structure, not decoration.** One `<h1>` matching
  the title's intent, `<h2>` per major section, in a real hierarchy - a
  crawler and a screen reader both read structure, not just words.
- **Structured data (JSON-LD), every build:**
  - `LocalBusiness` (or a specific subtype - `HealthClub`, `Restaurant`)
    whenever there's a real address or service area - name, address,
    phone/WhatsApp, hours, price range if public.
  - `FAQPage` whenever the site has an FAQ section - free rich-snippet
    space, the content already exists.
  - Never fabricate a field a schema asks for. Omit what the briefing
    doesn't have - same rule as everywhere else.
- **Standard files, every build:** `sitemap.xml` and `robots.txt` (allow
  all, point at the sitemap), in the project root beside `index.html` -
  even a one-page site benefits, it's what tells Google the canonical URL
  and last-modified date. `scripts/check.py` checks both exist.
- **Canonical tag, always** - `<link rel="canonical" href="...">` pointing
  at the real published URL once known; the client's domain, never a
  staging or preview URL.
- **Local SEO beyond the code:** the real address as visible text
  somewhere on the page, not only inside an image or a map embed - crawlers
  don't read pixels. A real link to the Google Maps listing if one exists.
  Name/address/phone consistent everywhere they appear.

## Avoiding the generated look

The banned list in `taste.md` is the hard floor. Beyond it:

- **One deliberate, specific choice per site** that no template would make -
  an unusual type pairing, an asymmetric hero, a colour taken from the
  client's actual premises, a section only this business could have.
- **Break the grid at least once,** on purpose, where it means something.
- **Vary section rhythm.** Not every section is centred text over an image.
  Alternate alignment, density, and background.
- **Content, not slots.** Write the real sections this business needs. Never
  "Our Values / Our Mission / Why Choose Us" scaffolding filled in afterwards.
- **No decorative abstractions:** floating blobs, mesh gradients, 3D shapes,
  glassmorphism panels, dot grids as texture.
- Specificity is the whole defence. A site that names the street, shows the
  actual room and quotes a real customer cannot look generated.
