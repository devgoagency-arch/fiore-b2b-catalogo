import sys
with open('src/components/Catalogue.astro', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = '''let activeCategory = CATEGORIES.length > 0 ? CATEGORIES[0] : '';
let activeSearch = '';
let currentPage = 1;
const pageSize = 20;

window.handleSearch = function(query) {
  activeSearch = (query || '').toLowerCase().trim();
  
  const topInput = document.getElementById('global-search-top');
  const catInput = document.getElementById('global-search-cat');
  const mobInput = document.getElementById('global-search-mobile');
  
  if (topInput && topInput.value !== query) topInput.value = query;
  if (catInput && catInput.value !== query) catInput.value = query;
  if (mobInput && mobInput.value !== query) mobInput.value = query;

  currentPage = 1;
  renderProducts(false);
};

function getFilteredProducts() {
  return PRODUCTS.filter(p => {
    const catMatch = activeCategory === 'All' || p.category === activeCategory;
    let searchMatch = true;
    if (activeSearch) {
      const searchString = \\ \ \\.toLowerCase();
      searchMatch = searchString.includes(activeSearch);
    }
    return catMatch && searchMatch;
  });
}

function renderFilters() {
  const cats = ['All', ...CATEGORIES];
  
  const desktopContainer = document.getElementById('category-filters-desktop');
  if(desktopContainer) {
    desktopContainer.innerHTML = cats.map(c => \
      <button onclick="filterProducts('\')" type="button" class="btn \ px-5 py-2 text-sm font-rob whitespace-nowrap">\</button>
    \).join('');
  }

  const mobileLabel = document.getElementById('mobile-category-label');
  const mobileDropdown = document.getElementById('mobile-category-dropdown');
  if(mobileLabel && mobileDropdown) {
    mobileLabel.textContent = \Filter by Category: \\;
    mobileDropdown.innerHTML = cats.map(c => \
      <button onclick="filterProducts('\'); toggleMobileCategories();" type="button" class="w-full text-left px-4 py-3 text-sm font-rob border-b border-gray-50 last:border-0 \">\</button>
    \).join('');
  }
}

function toggleMobileCategories() {
  const dropdown = document.getElementById('mobile-category-dropdown');
  if(dropdown) dropdown.classList.toggle('hidden');
}

function filterProducts(cat) {
  activeCategory = cat;
  currentPage = 1;
  renderFilters();
  renderProducts(false);
  const catalogue = document.getElementById('catalogue');
  if (catalogue) {
    const offset = catalogue.getBoundingClientRect().top + window.scrollY - 100;
    window.scrollTo({ top: offset, behavior: 'smooth' });
  }
}

function loadMoreProducts() {
  const filtered = getFilteredProducts();
  if (currentPage * pageSize >= filtered.length) return;
  currentPage++;
  renderProducts(true);
}

// -- Render product rows --
function renderProducts(append = false) {
  const filtered = getFilteredProducts();
  const end = currentPage * pageSize;
  
  const allRows = document.querySelectorAll('.prow');
  
  allRows.forEach(row => {
    const rowId = parseInt(row.getAttribute('data-id'));
    const p = PRODUCTS.find(x => x.id === rowId);
    
    if (p) {
      const index = filtered.findIndex(x => x.id === rowId);
      if (index !== -1 && index < end) {
        row.style.display = 'flex';
        row.classList.remove('hidden');
      } else {
'''

lines[281:348] = [new_content + '\n']

with open('src/components/Catalogue.astro', 'w', encoding='utf-8') as f:
    f.writelines(lines)
