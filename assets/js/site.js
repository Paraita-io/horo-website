(function () {
  const navToggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');

  if (navToggle && nav) {
    navToggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.focus();
      }
    });

    nav.addEventListener('click', (event) => {
      if (event.target instanceof HTMLAnchorElement) {
        nav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  const carousels = document.querySelectorAll('[data-carousel]');
  carousels.forEach((carousel) => {
    const track = carousel.querySelector('[data-carousel-track]');
    const prevBtn = carousel.querySelector('[data-carousel-prev]');
    const nextBtn = carousel.querySelector('[data-carousel-next]');

    if (!track || !prevBtn || !nextBtn) {
      return;
    }

    const scrollByCard = (direction) => {
      const card = track.firstElementChild;
      const gap = 12;
      const step = card ? card.getBoundingClientRect().width + gap : 260;
      track.scrollBy({ left: direction * step, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
    };

    prevBtn.addEventListener('click', () => scrollByCard(-1));
    nextBtn.addEventListener('click', () => scrollByCard(1));
  });
})();
