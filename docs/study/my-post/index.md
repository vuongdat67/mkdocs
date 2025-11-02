---
hide:
#   - navigation
  - toc
title: My Posts
---

# 📝 My Blog Posts

<div class="posts-container" id="postsContainer">
  <div class="posts-grid" id="postsGrid">
    <!-- Posts will be dynamically loaded here -->
  </div>
</div>

<style>
.posts-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.posts-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 24px;
  margin-top: 32px;
}

.post-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 12px;
  padding: 24px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.post-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  transform: scaleX(0);
  transition: transform 0.3s ease;
}

.post-card:hover::before {
  transform: scaleX(1);
}

.post-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(102, 234, 153, 0.2);
  border-color: #66ea85ff;
}

.post-card h3 {
  margin: 0 0 12px 0;
  font-size: 1.3rem;
  color: var(--md-typeset-a-color);
  line-height: 1.4;
}

.post-card .post-excerpt {
  color: var(--md-default-fg-color--light);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 16px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-card .post-meta {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  font-size: 0.85rem;
  color: var(--md-default-fg-color--lighter);
}

.post-tag {
  background: rgba(6, 112, 52, 0.1);
  color: #66ea9bff;
  padding: 4px 12px;
  border-radius: 12px;
  font-weight: 500;
}

[data-md-color-scheme="slate"] .post-card {
  background: var(--md-code-bg-color);
}

[data-md-color-scheme="slate"] .post-tag {
  background: rgba(102, 126, 234, 0.2);
  color: #a2ffb6ff;
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
  border-color: #66eabaff;
  box-shadow: 0 0 0 3px rgba(102, 234, 104, 0.1);
}

.posts-count {
  text-align: center;
  color: var(--md-default-fg-color--light);
  margin-top: 16px;
  font-size: 0.9rem;
}




@media (max-width: 768px) {
  .posts-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  
  .post-card {
    padding: 20px;
  }
}
</style>

<script>
// List of all posts in my-post folder
const posts = [
  {
    title: "Add Alembic Migrations to Existing FastAPI Ormar Project",
    slug: "add-alembic-migrations-to-existing-fastapi-ormar-project",
    excerpt: "Learn how to integrate Alembic database migrations into an existing FastAPI project using Ormar ORM.",
    tags: ["FastAPI", "Alembic", "Python", "Database"]
  },
  {
    title: "Adding Links to Formatted and Syntax Highlighted Code",
    slug: "adding-links-to-formatted-and-syntax-highlighted-code",
    excerpt: "Techniques for adding clickable links to syntax-highlighted code blocks in documentation.",
    tags: ["Documentation", "Code", "MkDocs"]
  },
  {
    title: "Challenge: Fill Space One Line 90 Degree Same Direction",
    slug: "challenge-fill-space-one-line-90-degree-same-direction",
    excerpt: "A programming challenge exploring creative ways to fill space with geometric constraints.",
    tags: ["Challenge", "Algorithm"]
  },
  {
    title: "Django Auth Server for Shiny",
    slug: "django-auth-server-for-shiny",
    excerpt: "Building an authentication server using Django to secure Shiny applications.",
    tags: ["Django", "Shiny", "Authentication"]
  },
  {
    title: "Django Dashboard with Suit and Highcharts",
    slug: "django-dashboard-with-suit-and-highcharts",
    excerpt: "Creating beautiful admin dashboards in Django using Django Suit and Highcharts.",
    tags: ["Django", "Dashboard", "Visualization"]
  },
  {
    title: "Docker Compose Django Postgres Nginx",
    slug: "docker-compose-django-postgres-nginx",
    excerpt: "Complete Docker Compose setup for Django applications with PostgreSQL and Nginx.",
    tags: ["Docker", "Django", "PostgreSQL", "Nginx"]
  },
  {
    title: "Documentation in Your Shell Scripts Using Shellman",
    slug: "documentation-in-your-shell-scripts-using-shellman",
    excerpt: "How to write and generate documentation for shell scripts using Shellman.",
    tags: ["Shell", "Documentation", "Shellman"]
  },
  {
    title: "Dual Screens Setup Nvidia BunsenLabs Debian Jessie",
    slug: "dual-screens-setup-nvidia-bunsenlabs-debian-jessie",
    excerpt: "Setting up dual monitors with Nvidia drivers on BunsenLabs Debian Jessie.",
    tags: ["Linux", "Nvidia", "Setup"]
  },
  {
    title: "How to Deal with Jinja2 Spacing",
    slug: "how-to-deal-with-jinja2-spacing",
    excerpt: "Tips and tricks for controlling whitespace in Jinja2 templates.",
    tags: ["Jinja2", "Templates", "Python"]
  },
  {
    title: "How to Edit Git Commit Contents",
    slug: "howto-edit-git-commit-contents",
    excerpt: "Guide to editing, amending, and rewriting Git commit history.",
    tags: ["Git", "Version Control"]
  },
  {
    title: "Local HTTP Server Fake Files Testing Purposes",
    slug: "local-http-server-fake-files-testing-purposes",
    excerpt: "Creating a local HTTP server with fake files for testing and development.",
    tags: ["Testing", "HTTP", "Development"]
  },
  {
    title: "Migrate Disqus Comments to Utterances GitHub",
    slug: "migrate-disqus-comments-to-utterances-github",
    excerpt: "Step-by-step guide to migrating from Disqus to Utterances for GitHub-based comments.",
    tags: ["Comments", "Migration", "GitHub"]
  },
  {
    title: "Pass Makefile Args as Typed in Command Line",
    slug: "pass-makefile-args-as-typed-in-command-line",
    excerpt: "How to pass arguments to Makefile targets exactly as typed in the command line.",
    tags: ["Make", "Build Tools"]
  },
  {
    title: "Plugins as Python Native Namespace Packages",
    slug: "plugins-as-python-native-namespace-packages",
    excerpt: "Implementing plugin systems using Python's native namespace packages.",
    tags: ["Python", "Plugins", "Architecture"]
  },
  {
    title: "Python Static Code Analysis Tools",
    slug: "python-static-code-analysis-tools",
    excerpt: "Overview of popular static code analysis tools for Python development.",
    tags: ["Python", "Code Quality", "Tools"]
  },
  {
    title: "Same Pytest Fixtures with Different Scopes",
    slug: "same-pytest-fixtures-with-different-scopes",
    excerpt: "Managing pytest fixtures with different scopes in your test suite.",
    tags: ["Python", "Pytest", "Testing"]
  },
  {
    title: "Save Pytest Logs as Artifact GitLab CI",
    slug: "save-pytest-logs-as-artifact-gitlab-ci",
    excerpt: "Configure GitLab CI to save pytest logs as artifacts for debugging.",
    tags: ["GitLab CI", "Pytest", "CI/CD"]
  },
  {
    title: "Somewhat Modern Python Development",
    slug: "somewhat-modern-python-development",
    excerpt: "Best practices and tools for modern Python development workflows.",
    tags: ["Python", "Best Practices", "Development"]
  },
  {
    title: "Steam Linux ALVR Quest 2",
    slug: "steam-linux-alvr-quest2",
    excerpt: "Playing Steam VR games on Linux with Quest 2 using ALVR.",
    tags: ["Linux", "VR", "Gaming"]
  },
  {
    title: "Testing FastAPI Ormar Alembic Apps",
    slug: "testing-fastapi-ormar-alembic-apps",
    excerpt: "Comprehensive testing strategies for FastAPI applications using Ormar and Alembic.",
    tags: ["FastAPI", "Testing", "Python"]
  },
  {
    title: "The Insiders Journey",
    slug: "the-insiders-journey",
    excerpt: "My experience and journey with the MkDocs Material Insiders program.",
    tags: ["MkDocs", "Insiders", "Experience"]
  },
  {
    title: "Tingling Sensation Witnessing Existence",
    slug: "tingling-sensation-witnessing-existence",
    excerpt: "Philosophical reflections on consciousness and existence.",
    tags: ["Philosophy", "Reflection"]
  },
  {
    title: "Tips for Writing Good Python CLI Libraries",
    slug: "tips-for-writing-good-python-cli-libraries",
    excerpt: "Best practices for creating user-friendly Python command-line interfaces.",
    tags: ["Python", "CLI", "Best Practices"]
  },
  {
    title: "Unify Logging for a Gunicorn Uvicorn App",
    slug: "unify-logging-for-a-gunicorn-uvicorn-app",
    excerpt: "Standardizing logging across Gunicorn and Uvicorn in production applications.",
    tags: ["Python", "Logging", "Gunicorn", "Uvicorn"]
  },
  {
    title: "Write and Use a Tox Plugin from Inside Your Package",
    slug: "write-and-use-a-tox-plugin-from-inside-your-package",
    excerpt: "Creating and integrating Tox plugins directly within your Python package.",
    tags: ["Python", "Tox", "Plugins"]
  }
];

function createPostCard(post) {
  const card = document.createElement('a');
  card.href = post.slug + '/';
  card.className = 'post-card';
  card.style.textDecoration = 'none';
  
  const title = document.createElement('h3');
  title.textContent = post.title;
  
  const excerpt = document.createElement('p');
  excerpt.className = 'post-excerpt';
  excerpt.textContent = post.excerpt;
  
  const meta = document.createElement('div');
  meta.className = 'post-meta';
  
  post.tags.forEach(tag => {
    const tagEl = document.createElement('span');
    tagEl.className = 'post-tag';
    tagEl.textContent = tag;
    meta.appendChild(tagEl);
  });
  
  card.appendChild(title);
  card.appendChild(excerpt);
  card.appendChild(meta);
  
  return card;
}

function renderPosts(filteredPosts) {
  const container = document.getElementById('postsGrid');
  container.innerHTML = '';
  
  filteredPosts.forEach(post => {
    container.appendChild(createPostCard(post));
  });
  
  updateCount(filteredPosts.length);
}

function updateCount(count) {
  let countEl = document.querySelector('.posts-count');
  if (!countEl) {
    countEl = document.createElement('div');
    countEl.className = 'posts-count';
    document.getElementById('postsContainer').appendChild(countEl);
  }
  countEl.textContent = `Showing ${count} of ${posts.length} posts`;
}

function filterPosts(searchTerm) {
  const term = searchTerm.toLowerCase();
  return posts.filter(post => 
    post.title.toLowerCase().includes(term) ||
    post.excerpt.toLowerCase().includes(term) ||
    post.tags.some(tag => tag.toLowerCase().includes(term))
  );
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  // Add search box
  const searchBox = document.createElement('div');
  searchBox.className = 'search-box';
  searchBox.innerHTML = '<input type="text" id="postSearch" placeholder="🔍 Search posts by title, description, or tags...">';
  
  const container = document.getElementById('postsContainer');
  container.insertBefore(searchBox, container.firstChild);
  
  // Add search functionality
  document.getElementById('postSearch').addEventListener('input', function(e) {
    const filtered = filterPosts(e.target.value);
    renderPosts(filtered);
  });
  
  // Initial render
  renderPosts(posts);
});
</script>
