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

// Header search autocomplete
(function() {
  const form = document.querySelector('.header__search[data-suggest-url]');
  if (!form) return;
  const input = form.querySelector('.header__search-input');
  const box = form.querySelector('.header__suggest');
  const url = form.dataset.suggestUrl;
  let timer = null;
  let lastQuery = '';
  let activeIndex = -1;

  function escapeHTML(str) {
    return String(str).replace(/[&<>"']/g, m => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
    })[m]);
  }

  function hide() {
    box.hidden = true;
    box.innerHTML = '';
    activeIndex = -1;
  }

  function render(query, results) {
    if (!results.length) {
      box.innerHTML = '<div class="header__suggest-empty">Sin resultados para "' + escapeHTML(query) + '"</div>';
    } else {
      let html = '';
      results.forEach(r => {
        const img = r.imagen
          ? '<img src="' + encodeURI(r.imagen) + '" alt="">'
          : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#001530" stroke-width="2"><circle cx="11" cy="11" r="8"/></svg>';
        html += '<a class="header__suggest-item" href="' + r.url + '">'
              +   '<div class="header__suggest-thumb">' + img + '</div>'
              +   '<div class="header__suggest-body">'
              +     '<div class="header__suggest-name">' + escapeHTML(r.nombre) + '</div>'
              +     '<div class="header__suggest-meta">' + escapeHTML(r.categoria) + ' / ' + escapeHTML(r.subcategoria) + '</div>'
              +   '</div>'
              +   '<span class="header__suggest-code">' + escapeHTML(r.codigo) + '</span>'
              + '</a>';
      });
      html += '<a class="header__suggest-footer" href="/buscar/?q=' + encodeURIComponent(query) + '">Ver todos los resultados &rsaquo;</a>';
      box.innerHTML = html;
    }
    box.hidden = false;
    activeIndex = -1;
  }

  function fetchSuggest(query) {
    if (query === lastQuery) return;
    lastQuery = query;
    fetch(url + '?q=' + encodeURIComponent(query), { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
      .then(r => r.json())
      .then(data => {
        if (input.value.trim() !== query) return; // outdated
        render(query, data.results || []);
      })
      .catch(() => {});
  }

  input.addEventListener('input', () => {
    const q = input.value.trim();
    clearTimeout(timer);
    if (q.length < 2) {
      hide();
      lastQuery = '';
      return;
    }
    timer = setTimeout(() => fetchSuggest(q), 180);
  });

  input.addEventListener('focus', () => {
    if (input.value.trim().length >= 2 && box.innerHTML) {
      box.hidden = false;
    }
  });

  input.addEventListener('keydown', (e) => {
    if (box.hidden) return;
    const items = box.querySelectorAll('.header__suggest-item');
    if (!items.length) return;
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeIndex = (activeIndex + 1) % items.length;
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeIndex = activeIndex <= 0 ? items.length - 1 : activeIndex - 1;
    } else if (e.key === 'Enter' && activeIndex >= 0) {
      e.preventDefault();
      window.location.href = items[activeIndex].href;
      return;
    } else if (e.key === 'Escape') {
      hide();
      return;
    } else {
      return;
    }
    items.forEach((el, i) => el.classList.toggle('is-active', i === activeIndex));
    items[activeIndex].scrollIntoView({ block: 'nearest' });
  });

  document.addEventListener('click', (e) => {
    if (!form.contains(e.target)) hide();
  });
})();
