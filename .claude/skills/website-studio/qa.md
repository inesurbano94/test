# Final visual QA

Load at phase 5 only. Work it top to bottom on the real, rendered site - not
by reading the code. Fix as you go. Report what was found and fixed.

## 1. Truth

- [ ] Every fact, price, claim, credential and statistic traces to the briefing
- [ ] No invented testimonials, review counts or years in business
- [ ] Anything placeholder is marked in the HTML **and** listed in the README
- [ ] Phone, WhatsApp, email, address and hours are correct and identical
      everywhere they appear
- [ ] Every external link opens the right place; social links are the client's

## 2. First impression

Look at the hero for three seconds and answer: what is this business, where,
and what do I do next? If any answer is unclear, the hero fails.

- [ ] The primary action is visible without scrolling
- [ ] The strongest available photo is the one being used biggest
- [ ] Nothing on screen is a placeholder

## 3. Type

- [ ] Two families maximum, consistent weights throughout
- [ ] No paragraph wider than ~75 characters
- [ ] Heading hierarchy is visible at a squint - h1 vs h2 vs h3 unmistakable
- [ ] No orphaned single words on their own line in headings
- [ ] Body text at least 16px everywhere, including captions and footer

## 4. Space and rhythm

- [ ] Section padding consistent, generous, from the scale
- [ ] Headings sit closer to their own content than to the block above
- [ ] No accidental double gaps or collapsed margins
- [ ] Sections vary in rhythm - not the same centred layout repeating

## 5. Colour and image

- [ ] One accent doing the emphasis work; nothing competing
- [ ] Body text contrast ≥ 4.5:1, large text ≥ 3:1 - checked, not assumed
- [ ] Text over images stays readable at every breakpoint
- [ ] No weak photo used large
- [ ] Photos read as one set - consistent grade and crop logic
- [ ] Every image has real alt text or `alt=""` if decorative

## 6. Responsive

Check at 360, 390, 768, 1024, 1440.

- [ ] No horizontal scroll at any width, especially 360
- [ ] Nothing overflows, overlaps or gets clipped
- [ ] Tap targets ≥ 44px, with space between them
- [ ] Mobile menu opens, closes, traps focus, and closes on link click
- [ ] Sticky elements do not cover content or eat the viewport
- [ ] Long pt-PT words do not break the layout

## 7. Motion

- [ ] Reveals fire once, do not repeat on scroll back
- [ ] Nothing is invisible if JS fails - no content trapped at opacity 0
- [ ] `prefers-reduced-motion: reduce` genuinely disables it - test it
- [ ] No animation over ~600ms, no bouncy easing
- [ ] Nothing shifts layout after load (check CLS by eye on a slow reload)

## 8. Interaction

- [ ] Every interactive element has hover, focus-visible and active states
- [ ] Tab through the whole page: order is logical, focus always visible
- [ ] Anchor links land with the heading clear of the sticky header
- [ ] Forms: labels, correct input types, visible errors, working submit
- [ ] WhatsApp links open the right number with the right prefilled message

## 9. Technical

- [ ] `<title>` and `<meta name="description">` written for this business,
      including the location
- [ ] Open Graph title, description and image - previewed as a shared link
- [ ] Favicon present at all sizes
- [ ] `<html lang="">` correct; hreflang correct and reciprocal if bilingual
- [ ] Images `.webp`, sized to display width, lazy below the fold
- [ ] Console clean - no errors, no 404s
- [ ] One `<h1>` per page; landmarks (`header`, `main`, `footer`, `nav`) used
- [ ] `LocalBusiness` JSON-LD present if it has premises or a service area
- [ ] `FAQPage` JSON-LD present if the site has an FAQ section
- [ ] Canonical `<link>` present, pointing at the real published URL
- [ ] `sitemap.xml` and `robots.txt` present in the project root
- [ ] `scripts/check.py` run and its `seo` findings addressed - see
      `guidelines.md`'s SEO section

## 10. The generated-look sweep

Read `taste.md`'s banned list, then ask honestly:

- [ ] Could this page be any other business? If yes, it is not finished
- [ ] Is there at least one choice here no template would make?
- [ ] Any purple/blue gradient, glow, emoji icon, or meaningless icon row?
- [ ] Any sentence that is premium filler rather than information?
- [ ] Does it look like Inés made it, or like a model made it?

## 11. Handover

- [ ] README lists: what is placeholder, what is needed from the client,
      how to publish, where to change the phone number
- [ ] Shot list included if photos are still outstanding

## 12. Taste

- [ ] Read `.website-studio-learnings.md`, present the captured signals, ask
      what to keep, append the approved ones to `taste.md` with today's date
