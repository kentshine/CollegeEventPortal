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

// Slider


function removeFlash() {
  const element = document.getElementById("popup");
  element.remove();
}

appShots.forEach((el) => scrollObserver.observe(el));
