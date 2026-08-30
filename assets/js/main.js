(function () {
  "use strict";

  // Single source of truth for the WhatsApp number. Placeholder — see README.
  var WHATSAPP_NUMBER = "351900000000";
  var waLinks = document.querySelectorAll('a[href*="wa.me/351900000000"]');
  waLinks.forEach(function (a) {
    var text = a.getAttribute("data-wa-text");
    var url = "https://wa.me/" + WHATSAPP_NUMBER + (text ? "?text=" + encodeURIComponent(text) : "");
    a.setAttribute("href", url);
  });

  // Mobile nav
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  if (header && toggle) {
    toggle.addEventListener("click", function () {
      var isOpen = header.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(isOpen));
    });
    header.querySelectorAll(".nav__links a").forEach(function (link) {
      link.addEventListener("click", function () {
        header.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Scroll reveal
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry, i) {
          if (entry.isIntersecting) {
            setTimeout(function () {
              entry.target.classList.add("is-visible");
            }, (i % 6) * 70);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  // Hide floating WhatsApp button once the footer CTA is in view
  var fab = document.querySelector(".fab");
  var ctaFinal = document.querySelector(".cta-final");
  if (fab && ctaFinal && "IntersectionObserver" in window) {
    var fabObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          fab.style.opacity = entry.isIntersecting ? "0" : "1";
          fab.style.pointerEvents = entry.isIntersecting ? "none" : "auto";
        });
      },
      { threshold: 0.3 }
    );
    fabObserver.observe(ctaFinal);
  }
})();
