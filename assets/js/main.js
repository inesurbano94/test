(() => {
  "use strict";

  /* ----------------------------------------------------------
     Single source of truth for the WhatsApp number.
     Format: country code + number, no spaces, no "+".
     e.g. Portugal mobile -> "351912345678"
     TODO: replace with the real number before launch.
  ---------------------------------------------------------- */
  const WHATSAPP_NUMBER = "351900000000";
  const DEFAULT_MESSAGE = "Olá Isaías, gostava de saber mais sobre o treino personalizado.";

  document.querySelectorAll("[data-whatsapp]").forEach((el) => {
    const msg = el.getAttribute("data-whatsapp") || DEFAULT_MESSAGE;
    el.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`;
  });

  /* ---------------- Nav scroll state ---------------- */
  const nav = document.getElementById("nav");
  const onScroll = () => {
    nav.classList.toggle("is-scrolled", window.scrollY > 40);
    fab.classList.toggle("is-visible", window.scrollY > window.innerHeight * 0.6);
  };

  /* ---------------- Mobile menu ---------------- */
  const burger = document.getElementById("burger");
  const closeMenu = () => {
    document.body.classList.remove("menu-open");
    burger.setAttribute("aria-expanded", "false");
  };
  burger.addEventListener("click", () => {
    const open = document.body.classList.toggle("menu-open");
    burger.setAttribute("aria-expanded", String(open));
  });
  document.querySelectorAll(".mobile-menu a").forEach((a) => a.addEventListener("click", closeMenu));

  /* ---------------- Floating WhatsApp button ---------------- */
  const fab = document.getElementById("fab");
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------------- Reveal on scroll ---------------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  /* ---------------- Footer year ---------------- */
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---------------- Resultados testimonial rail ---------------- */
  const rail = document.getElementById("resultadosRail");
  const railPrev = document.getElementById("resultadosPrev");
  const railNext = document.getElementById("resultadosNext");
  if (rail && railPrev && railNext) {
    const cardStep = () => {
      const card = rail.querySelector(".testimonial");
      if (!card) return rail.clientWidth;
      const gap = parseFloat(getComputedStyle(rail).columnGap || 0);
      return card.getBoundingClientRect().width + gap;
    };
    const updateRailNav = () => {
      const max = rail.scrollWidth - rail.clientWidth - 1;
      railPrev.disabled = rail.scrollLeft <= 0;
      railNext.disabled = rail.scrollLeft >= max;
      rail.classList.toggle("is-end", rail.scrollLeft >= max);
    };
    railPrev.addEventListener("click", () => rail.scrollBy({ left: -cardStep(), behavior: "smooth" }));
    railNext.addEventListener("click", () => rail.scrollBy({ left: cardStep(), behavior: "smooth" }));
    rail.addEventListener("scroll", updateRailNav, { passive: true });
    window.addEventListener("resize", updateRailNav);
    updateRailNav();
  }
})();
