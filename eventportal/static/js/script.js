/* FOR CURRENT YEAR */
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
yearEl.textContent = currentYear;

/* HOVER FUNCTIONALITY FOR MOBILE */
document.addEventListener("touchstart", function () {}, true);

/* HAMBURGER MENU */
const navButton = document.querySelector(".mobile-nav-btn");
const headerElement = document.querySelector(".header");

navButton.addEventListener("click", function () {
  headerElement.classList.toggle("nav-open");
});

/* SMOOTH SCROLLING */
const links = document.querySelectorAll("a:not(.footer-link)");

links.forEach(function (link) {
  link.addEventListener("click", function (el) {
    el.preventDefault();
    /* LINKS */
    const href = link.getAttribute("href");
    if (href === "#")
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

    if (href !== "#" && href.startsWith("#")) {
      const sectionElement = document.querySelector(href);
      sectionElement.scrollIntoView({ behavior: "smooth" });
    }
    /* CLOSE MENU ON CLICK */
    if (link.classList.contains("nav-link")) {
      headerElement.classList.toggle("nav-open");
    }
  });
});

/* STICKY NAVIGATION */
const heroElement = document.querySelector(".section-hero");
const navObserver = new IntersectionObserver(
  function (entries) {
    const ent = entries[0];
    if (ent.isIntersecting === false) {
      document.body.classList.add("sticky");
    } else {
      document.body.classList.remove("sticky");
    }
  },
  {
    root: null,
    threshold: 0,
    rootMargin: "-80px",
  }
);

navObserver.observe(heroElement);

/* SCROLL ANIMATE */
const appShots = document.querySelectorAll(".mobile-bg");
const scrollObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("animate-img");
    } else {
      entry.target.classList.remove("animate-img");
    }
  });
});

appShots.forEach((el) => scrollObserver.observe(el));
