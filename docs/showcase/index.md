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

/* Also remove padding from main container */
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
}

.project-card:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
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
}

.project-card .project-description {
  padding: 0 24px 16px;
  color: var(--md-default-fg-color--light);
  font-size: 0.95rem;
  line-height: 1.6;
  margin: 16px 0 0 0;
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
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0;
}

.project-footer {
  padding: 16px 20px;
  border-top: 1px solid var(--md-default-fg-color--lightest);
  display: flex;
  gap: 8px;
  justify-content: center;
}

.github-btn {
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

.github-btn:hover {
  background: #4a9eff;
  color: white;
  transform: translateY(-1px);
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
    description: "It's a command line client for aria2. It features a nice TUI!",
    image: "golang.png",
    github: "https://github.com/",
    docs: ""
  },
  {
    name: "mkdocstrings",
    title: "mkdocstrings",
    description: "Automatic documentation from sources, for MkDocs.",
    image: "golang.png",
    github: "",
    docs: ""
  },
  {
    name: "mkdocstrings",
    title: "mkdocstrings",
    description: "Automatic documentation from sources, for MkDocs.",
    image: "golang.png",
    github: "",
    docs: ""
  },
  {
    name: "griffe",
    title: "griffe",
    description: "API signatures for entire Python programs.",
    image: "golang.png",
    github: "https://github.com/mkdocstrings/griffe",
    docs: "https://mkdocstrings.github.io/griffe/"
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
  
  // Image section
  const imageDiv = document.createElement('div');
  imageDiv.className = 'project-image';
  
  const img = document.createElement('img');
  // Images are in showcase/images/ folder
  img.src = `images/${project.image}`;
  img.alt = project.title;
  img.loading = 'lazy';
  imageDiv.appendChild(img);
  
  // Footer with GitHub button
  const footer = document.createElement('div');
  footer.className = 'project-footer';
  
  if (project.github) {
    const githubBtn = document.createElement('a');
    githubBtn.href = project.github;
    githubBtn.className = 'github-btn';
    githubBtn.target = '_blank';
    githubBtn.innerHTML = `
      <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
      </svg>
      GitHub
    `;
    footer.appendChild(githubBtn);
    
    // Prevent card click when clicking GitHub button
    githubBtn.addEventListener('click', (e) => {
      e.stopPropagation();
    });
  }
  
  card.appendChild(header);
  card.appendChild(description);
  card.appendChild(imageDiv);
//   card.appendChild(footer);
  
  // Make whole card clickable to local page
  card.style.cursor = 'pointer';
  card.addEventListener('click', () => {
    // Link to local markdown file (e.g., showcase/aria2p/)
    window.location.href = `${project.name}/`;
  });
  
  return card;
}

function renderProjects(filteredProjects) {
  const container = document.getElementById('showcaseGrid');
  container.innerHTML = '';
  
  filteredProjects.forEach(project => {
    container.appendChild(createProjectCard(project));
  });
  
  updateCount(filteredProjects.length);
}

function updateCount(count) {
  let countEl = document.querySelector('.projects-count');
  if (!countEl) {
    countEl = document.createElement('div');
    countEl.className = 'projects-count';
    document.getElementById('showcaseContainer').appendChild(countEl);
  }
  countEl.textContent = `Showing ${count} of ${projects.length} projects`;
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
  
  // Add search functionality
  document.getElementById('projectSearch').addEventListener('input', function(e) {
    const filtered = filterProjects(e.target.value);
    renderProjects(filtered);
  });
  
  // Initial render
  renderProjects(projects);
});
</script>
