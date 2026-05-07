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

// Professions carousel arrows
document.addEventListener('DOMContentLoaded', function() {
  var container = document.querySelector('.professions__inner');
  var leftBtn = document.querySelector('.professions__arrow--left');
  var rightBtn = document.querySelector('.professions__arrow--right');
  if (!container || !leftBtn || !rightBtn) return;

  var scrollAmount = 200;

  leftBtn.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    container.scrollLeft -= scrollAmount;
  });

  rightBtn.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    container.scrollLeft += scrollAmount;
  });

  function updateArrows() {
    if (container.scrollLeft <= 0) {
      leftBtn.style.opacity = '0';
      leftBtn.style.pointerEvents = 'none';
    } else {
      leftBtn.style.opacity = '1';
      leftBtn.style.pointerEvents = 'auto';
    }
    if (container.scrollLeft + container.clientWidth >= container.scrollWidth - 2) {
      rightBtn.style.opacity = '0';
      rightBtn.style.pointerEvents = 'none';
    } else {
      rightBtn.style.opacity = '1';
      rightBtn.style.pointerEvents = 'auto';
    }
  }

  container.addEventListener('scroll', updateArrows);
  window.addEventListener('resize', updateArrows);
  updateArrows();
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
