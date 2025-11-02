---
hide:
  - navigation
  - toc
title: Showcase
---

<div style="padding: 24px; text-align: center;">
  <h1 style="margin-top: 0;">🚀 My Projects Showcase</h1>
</div>

<div class="showcase-container" id="showcaseContainer">
  <div class="showcase-grid" id="showcaseGrid">
    <!-- Projects will be dynamically loaded here -->
  </div>
</div>

<style>
/* Main page title - no counter */
.md-content__inner > h1:first-of-type {
  counter-reset: none;
}

.md-content__inner > h1:first-of-type:before {
  content: none !important;
}

/* Remove default padding to maximize space */
.md-content__inner {
  padding: 0 !important;
  margin: 0 auto;
}

.md-content {
  max-width: 100% !important;
}

.md-main__inner {
  margin: 0 !important;
  padding: 0 !important;
}

.md-grid {
  max-width: none !important;
  margin: 0 !important;
  padding: 0 !important;
}

.showcase-container {
  max-width: 1600px;
  margin: 0 auto;
  padding: 40px 24px;
}

.showcase-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 32px;
}

.project-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  padding: 0;
  transition: all 0.3s ease;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100%;
  cursor: pointer;
  will-change: transform;
}

.project-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  transform: translateY(-4px);
}

.project-header {
  padding: 20px 24px 16px;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.project-card h3 {
  margin: 0;
  font-size: 1.25rem;
  color: #4a9eff;
  font-weight: 600;
  line-height: 1.4;
  transition: color 0.2s ease;
}

.project-card:hover h3 {
  color: #667eea;
}

.project-card .project-description {
  padding: 0 24px 16px;
  color: var(--md-default-fg-color--light);
  font-size: 0.95rem;
  line-height: 1.6;
  margin: 16px 0 0 0;
  flex: 1;
}

.project-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: var(--md-code-bg-color);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: relative;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0;
  transition: transform 0.3s ease;
}

.project-card:hover .project-image img {
  transform: scale(1.05);
}

.project-image.loading {
  background: linear-gradient(90deg, var(--md-code-bg-color) 25%, var(--md-default-fg-color--lightest) 50%, var(--md-code-bg-color) 75%);
  background-size: 200% 100%;
  animation: loading 1.5s ease-in-out infinite;
}

@keyframes loading {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.project-footer {
  padding: 16px 20px;
  border-top: 1px solid var(--md-default-fg-color--lightest);
  display: flex;
  gap: 8px;
  justify-content: center;
  flex-wrap: wrap;
}

.github-btn, .docs-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: transparent;
  border: 1.5px solid #4a9eff;
  border-radius: 6px;
  color: #4a9eff;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;
}

.github-btn:hover, .docs-btn:hover {
  background: #4a9eff;
  color: white;
  transform: translateY(-1px);
}

.docs-btn {
  border-color: #667eea;
  color: #667eea;
}

.docs-btn:hover {
  background: #667eea;
}

[data-md-color-scheme="slate"] .project-footer {
  border-top-color: #333;
}

[data-md-color-scheme="slate"] .project-card {
  background: #1e1e1e;
  border-color: #333;
}

[data-md-color-scheme="slate"] .project-header {
  border-bottom-color: #333;
}

[data-md-color-scheme="slate"] .project-image {
  background: #0d1117;
}

.search-box {
  margin-bottom: 24px;
  display: flex;
  justify-content: center;
}

.search-box input {
  width: 100%;
  max-width: 600px;
  padding: 12px 20px;
  font-size: 1rem;
  border: 2px solid var(--md-default-fg-color--lightest);
  border-radius: 24px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  transition: all 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.projects-count {
  text-align: center;
  color: var(--md-default-fg-color--light);
  margin-top: 16px;
  font-size: 0.9rem;
}

.no-results {
  text-align: center;
  padding: 60px 20px;
  color: var(--md-default-fg-color--light);
}

.no-results h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

@media (max-width: 1200px) {
  .showcase-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .showcase-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .showcase-container {
    padding: 24px 16px;
  }
  
  .project-image {
    min-height: 250px;
  }
  
  .search-box input {
    max-width: 100%;
  }
}
</style>

<script>
// List of all showcase projects
const projects = [
  {
    name: "aria2p",
    title: "aria2p",
    description: "Command-line client for aria2 with beautiful TUI interface.",
    image: "golang.png",
    github: "https://github.com/username/aria2p",
    docs: "https://aria2p.readthedocs.io"
  },
  {
    name: "mkdocstrings",
    title: "mkdocstrings",
    description: "Automatic documentation from sources, for MkDocs.",
    image: "python.png",
    github: "https://github.com/mkdocstrings/mkdocstrings",
    docs: "https://mkdocstrings.github.io"
  },
  {
    name: "griffe",
    title: "griffe",
    description: "API signatures for entire Python programs. Extract and analyze Python code.",
    image: "python.png",
    github: "https://github.com/mkdocstrings/griffe",
    docs: "https://mkdocstrings.github.io/griffe/"
  },
  {
    name: "security-toolkit",
    title: "Security Toolkit",
    description: "Comprehensive security tools for penetration testing and CTF challenges.",
    image: "security.png",
    github: "https://github.com/username/security-toolkit"
  },
];

function createProjectCard(project) {
  const card = document.createElement('div');
  card.className = 'project-card';
  
  // Header with title
  const header = document.createElement('div');
  header.className = 'project-header';
  
  const title = document.createElement('h3');
  title.textContent = project.title;
  header.appendChild(title);
  
  // Description
  const description = document.createElement('p');
  description.className = 'project-description';
  description.innerHTML = project.description;
  
  // Image section with loading state
  const imageDiv = document.createElement('div');
  imageDiv.className = 'project-image loading';
  
  const img = document.createElement('img');
  img.src = `images/${project.image}`;
  img.alt = project.title;
  img.loading = 'lazy';
  
  // Remove loading state when image loads
  img.onload = () => {
    imageDiv.classList.remove('loading');
  };
  
  // Fallback for missing images
  img.onerror = () => {
    imageDiv.classList.remove('loading');
    img.src = 'data:image/svg+xml,%3Csvg xmlns="http://www.w3.org/2000/svg" width="400" height="300"%3E%3Crect fill="%23f0f0f0" width="400" height="300"/%3E%3Ctext fill="%23999" font-family="sans-serif" font-size="24" dy="10.5" font-weight="bold" x="50%25" y="50%25" text-anchor="middle"%3ENo Image%3C/text%3E%3C/svg%3E';
  };
  
  imageDiv.appendChild(img);
  
  // Footer with buttons (only if github or docs exist)
  const footer = document.createElement('div');
  footer.className = 'project-footer';
  
  if (project.github) {
    const githubBtn = document.createElement('a');
    githubBtn.href = project.github;
    githubBtn.className = 'github-btn';
    githubBtn.target = '_blank';
    githubBtn.rel = 'noopener noreferrer';
    githubBtn.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
      </svg>
      GitHub
    `;
    footer.appendChild(githubBtn);
    
    githubBtn.addEventListener('click', (e) => {
      e.stopPropagation();
    });
  }
  
  if (project.docs) {
    const docsBtn = document.createElement('a');
    docsBtn.href = project.docs;
    docsBtn.className = 'docs-btn';
    docsBtn.target = '_blank';
    docsBtn.rel = 'noopener noreferrer';
    docsBtn.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
        <path d="M3 2.5a2.5 2.5 0 0 1 5 0V3h1v-.5a3.5 3.5 0 1 0-7 0V3H1v10.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5V3h-1v-.5a2.5 2.5 0 0 1 5 0V3h1v10.5a2.5 2.5 0 0 1-2.5 2.5h-11A2.5 2.5 0 0 1 0 13.5V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v1.5h-1V2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v11.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5V4H2v9.5z"/>
      </svg>
      Docs
    `;
    footer.appendChild(docsBtn);
    
    docsBtn.addEventListener('click', (e) => {
      e.stopPropagation();
    });
  }
  
  card.appendChild(header);
  card.appendChild(description);
  card.appendChild(imageDiv);
  
  // Only add footer if there are buttons
  if (project.github || project.docs) {
    card.appendChild(footer);
  }
  
  // Make whole card clickable to local page
  card.addEventListener('click', () => {
    window.location.href = `${project.name}/`;
  });
  
  return card;
}

function renderProjects(filteredProjects) {
  const container = document.getElementById('showcaseGrid');
  container.innerHTML = '';
  
  if (filteredProjects.length === 0) {
    const noResults = document.createElement('div');
    noResults.className = 'no-results';
    noResults.innerHTML = `
      <h3>No projects found</h3>
      <p>Try adjusting your search terms</p>
    `;
    container.appendChild(noResults);
  } else {
    filteredProjects.forEach(project => {
      container.appendChild(createProjectCard(project));
    });
  }
  
  updateCount(filteredProjects.length);
}

function updateCount(count) {
  let countEl = document.querySelector('.projects-count');
  if (!countEl) {
    countEl = document.createElement('div');
    countEl.className = 'projects-count';
    document.getElementById('showcaseContainer').appendChild(countEl);
  }
  countEl.textContent = `Showing ${count} of ${projects.length} project${projects.length !== 1 ? 's' : ''}`;
}

function filterProjects(searchTerm) {
  const term = searchTerm.toLowerCase();
  return projects.filter(project => 
    project.title.toLowerCase().includes(term) ||
    project.description.toLowerCase().includes(term) ||
    project.name.toLowerCase().includes(term)
  );
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  // Add search box
  const searchBox = document.createElement('div');
  searchBox.className = 'search-box';
  searchBox.innerHTML = '<input type="text" id="projectSearch" placeholder="🔍 Search projects by name or description...">';
  
  const container = document.getElementById('showcaseContainer');
  container.insertBefore(searchBox, container.firstChild);
  
  // Add search functionality with debounce
  let debounceTimer;
  document.getElementById('projectSearch').addEventListener('input', function(e) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const filtered = filterProjects(e.target.value);
      renderProjects(filtered);
    }, 300);
  });
  
  // Initial render
  renderProjects(projects);
});
</script>