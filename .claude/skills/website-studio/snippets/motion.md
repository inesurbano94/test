# Motion snippets

Working code, not prose to reimplement. Per taste principle T4 — motion is a
sign of life, not decoration — and the timing rules in `guidelines.md`
(expo-out `cubic-bezier(0.22, 1, 0.36, 1)`, 150-250ms for state changes,
350-450ms for reveals, `prefers-reduced-motion` always).

Read this at phase 4, alongside `guidelines.md`. Adapt tokens to the active
design system — these use `--ease` and generic names; swap in the project's
actual token names.

Every pattern here already respects `prefers-reduced-motion: reduce` in its
own CSS, in addition to the site-wide blanket rule guidelines.md requires.
Don't skip the site-wide rule because a snippet has its own — belt and
braces, some engines only honour one or the other reliably.

---

## 1. Scroll reveal

What was used on the Isaías rebuild. Fade + small rise, once, staggered.

```css
.reveal {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.5s var(--ease), transform 0.5s var(--ease);
}
.reveal.is-visible { opacity: 1; transform: translateY(0); }

@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```

```js
const revealEls = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add("is-visible"), (i % 4) * 70);
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
  revealEls.forEach((el) => io.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add("is-visible"));
}
```

Use for: section entrances, card grids (the `i % 4` caps stagger so a long
grid doesn't take seconds to finish revealing). Don't wrap an entire section
in one `.reveal` — reveal its children individually or it reads as a slab.

---

## 2. Magnetic hover lift

A card or button that leans toward the cursor. Restrained — a few degrees,
not a gimmick.

```css
.lift {
  transition: transform 0.3s var(--ease), box-shadow 0.3s var(--ease);
}
.lift:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 32px rgba(0,0,0,0.08);
}
@media (prefers-reduced-motion: reduce) {
  .lift { transition: none; }
  .lift:hover { transform: none; }
}
```

For a true cursor-follow tilt (use sparingly — one element type per page,
never on more than what's directly under the pointer):

```js
document.querySelectorAll(".lift--magnetic").forEach((el) => {
  el.addEventListener("mousemove", (e) => {
    const r = el.getBoundingClientRect();
    const x = ((e.clientX - r.left) / r.width - 0.5) * 6;
    const y = ((e.clientY - r.top) / r.height - 0.5) * -6;
    el.style.transform = `perspective(600px) rotateX(${y}deg) rotateY(${x}deg)`;
  });
  el.addEventListener("mouseleave", () => { el.style.transform = ""; });
});
```

Use for: a single hero feature card, a pricing card you want to feel
tactile. Never on body text or anything read closely — rotation fights
legibility.

---

## 3. Tab / panel switch

Content swap without a jump cut. Used for the Isaías pricing tabs.

```css
.panel { display: none; opacity: 0; }
.panel.active { display: block; animation: panel-in 0.35s var(--ease); }
@keyframes panel-in {
  from { opacity: 0; transform: translateY(6px); }
  to   { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .panel.active { animation: none; }
}
```

```js
tabs.forEach((tab) => {
  tab.addEventListener("click", () => {
    tabs.forEach((t) => t.classList.remove("active"));
    tab.classList.add("active");
    panels.forEach((p) => p.classList.remove("active"));
    document.getElementById(tab.dataset.target).classList.add("active");
  });
});
```

---

## 4. Marquee (logos, certifications, press mentions)

A slow, continuous drift — never a jarring loop-reset.

```css
.marquee { overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent, #000 8%, #000 92%, transparent); }
.marquee__track {
  display: flex;
  gap: 3rem;
  width: max-content;
  animation: marquee 28s linear infinite;
}
@keyframes marquee {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
@media (prefers-reduced-motion: reduce) {
  .marquee__track { animation: none; overflow-x: auto; }
}
```

```html
<div class="marquee">
  <div class="marquee__track">
    <!-- render the logo/cert list twice back to back, so -50% loops seamlessly -->
    <img src="..." alt="..."> <img src="..." alt="...">
    <img src="..." alt="..."> <img src="..." alt="...">
  </div>
</div>
```

Use for: certification badges, client logos, press names. Not for anything
that needs to be read carefully — a marquee is texture, not a reading task.

---

## 5. Orchestrated hero load-in

One considered moment on load, not scattered effects. Elements enter in a
deliberate order via staggered `animation-delay`, not all at once.

```css
.hero [data-in] {
  opacity: 0;
  transform: translateY(14px);
  animation: hero-in 0.6s var(--ease) forwards;
}
.hero [data-in="1"] { animation-delay: 0.05s; }
.hero [data-in="2"] { animation-delay: 0.15s; }
.hero [data-in="3"] { animation-delay: 0.25s; }
.hero [data-in="4"] { animation-delay: 0.35s; }
@keyframes hero-in {
  to { opacity: 1; transform: translateY(0); }
}
@media (prefers-reduced-motion: reduce) {
  .hero [data-in] { opacity: 1; transform: none; animation: none; }
}
```

```html
<div class="hero__kicker" data-in="1">...</div>
<h1 data-in="2">...</h1>
<p class="hero__lede" data-in="3">...</p>
<div class="hero__actions" data-in="4">...</div>
```

Use once per site, on the hero only. This is the "spend your boldness in one
place" move for motion — everywhere else stays quiet.

---

## Choosing among these

Not every site needs all five. Per guidelines.md: vary rhythm, don't reuse
the same trick everywhere. A reasonable default for a small-business site is
**#1 (scroll reveal) everywhere + #5 (hero load-in) once** — that alone
reads as considered. Add #2 or #3 only where the content structure actually
calls for it (a pricing comparison needs tabs; a features grid doesn't need
a magnetic hover). Reach for #4 only when there's a real logo/cert list to
show — it's decoration if invented.
