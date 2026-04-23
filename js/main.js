// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Tab switching
document.querySelectorAll('.products__tabs').forEach(tabGroup => {
  tabGroup.addEventListener('click', e => {
    if (e.target.classList.contains('products__tab')) {
      tabGroup.querySelectorAll('.products__tab').forEach(t => t.classList.remove('products__tab--active'));
      e.target.classList.add('products__tab--active');
    }
  });
});

// Header shrink on scroll
const header = document.querySelector('.header');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  if (currentScroll > 100) {
    header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.15)';
  } else {
    header.style.boxShadow = '0 1px 2px rgba(0,0,0,0.12)';
  }
  lastScroll = currentScroll;
});

// Simple search filter (visual only for static site)
const searchInput = document.querySelector('.header__search-input');
if (searchInput) {
  searchInput.addEventListener('keydown', e => {
    if (e.key === 'Enter') {
      const query = searchInput.value.trim().toLowerCase();
      if (query) {
        const catalogSection = document.getElementById('catalogo');
        if (catalogSection) {
          catalogSection.scrollIntoView({ behavior: 'smooth' });
        }
      }
    }
  });
}
