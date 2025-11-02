---
title: CTF Write-ups
hide:
  - navigation
  - toc
---

<div class="ctf-container">
  <!-- Header Section -->
  <div class="ctf-header">
    <h1>🏴‍☠️ CTF Write-ups</h1>
    <p class="ctf-subtitle">Capture The Flag challenges và lời giải chi tiết</p>
  </div>

  <!-- Stats Overview -->
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-icon">🎯</div>
      <div class="stat-number" id="total-challenges">0</div>
      <div class="stat-label">Total Challenges</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">✅</div>
      <div class="stat-number" id="solved-challenges">0</div>
      <div class="stat-label">Solved</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">🏆</div>
      <div class="stat-number" id="easy-count">0</div>
      <div class="stat-label">Easy Wins</div>
    </div>
    <div class="stat-card">
      <div class="stat-icon">⚡</div>
      <div class="stat-number" id="hard-count">0</div>
      <div class="stat-label">Hard Solves</div>
    </div>
  </div>

  <!-- Search & Filter Section -->
  <div class="filter-section">
    <div class="search-box">
      <input type="text" id="ctf-search" placeholder="🔍 Tìm kiếm challenge..." />
    </div>
    
    <div class="filter-group">
      <label>Category:</label>
      <select id="category-filter">
        <option value="all">All Categories</option>
        <option value="web">Web Exploitation</option>
        <option value="crypto">Cryptography</option>
        <option value="pwn">Binary Exploitation</option>
        <option value="reverse">Reverse Engineering</option>
        <option value="forensics">Forensics</option>
        <option value="misc">Miscellaneous</option>
      </select>
    </div>

    <div class="filter-group">
      <label>Difficulty:</label>
      <select id="difficulty-filter">
        <option value="all">All Levels</option>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
    </div>

    <div class="filter-group">
      <label>Sort by:</label>
      <select id="sort-by">
        <option value="date-desc">Newest First</option>
        <option value="date-asc">Oldest First</option>
        <option value="name-asc">Name A-Z</option>
        <option value="name-desc">Name Z-A</option>
        <option value="difficulty">Difficulty</option>
      </select>
    </div>
  </div>

  <!-- Challenges Grid -->
  <div id="challenges-grid" class="challenges-grid"></div>

  <!-- No Results -->
  <div id="no-results" class="no-results" style="display: none;">
    <div class="no-results-icon">🔍</div>
    <h3>Không tìm thấy challenge nào</h3>
    <p>Thử thay đổi bộ lọc hoặc từ khóa tìm kiếm</p>
  </div>
</div>

<style>
/* Container Styles */
.md-content__inner {
  padding: 0 !important;
  max-width: 100% !important;
}

.md-main__inner {
  padding: 0 !important;
}

.md-grid {
  max-width: 100% !important;
  padding: 0 !important;
}

.ctf-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 40px 20px;
}

/* Header */
.ctf-header {
  text-align: center;
  margin-bottom: 40px;
}

.ctf-header h1 {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 10px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.ctf-subtitle {
  font-size: 1.2rem;
  color: #666;
  margin: 0;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-card {
  background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
  border: 2px solid rgba(102, 126, 234, 0.3);
  border-radius: 15px;
  padding: 25px;
  text-align: center;
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.2);
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 5px;
}

.stat-label {
  font-size: 0.95rem;
  color: #666;
  font-weight: 500;
}

/* Filter Section */
.filter-section {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 40px;
  padding: 25px;
  background: var(--md-code-bg-color);
  border-radius: 15px;
  border: 1px solid rgba(102, 126, 234, 0.2);
}

.search-box {
  flex: 1 1 300px;
}

.search-box input {
  width: 100%;
  padding: 12px 20px;
  font-size: 1rem;
  border: 2px solid rgba(102, 126, 234, 0.3);
  border-radius: 25px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  transition: all 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 10px;
}

.filter-group label {
  font-weight: 600;
  font-size: 0.95rem;
  color: #666;
  white-space: nowrap;
}

.filter-group select {
  padding: 10px 15px;
  font-size: 0.95rem;
  border: 2px solid rgba(102, 126, 234, 0.3);
  border-radius: 20px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-group select:focus {
  outline: none;
  border-color: #667eea;
}

/* Challenges Grid */
.challenges-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 25px;
  margin-bottom: 40px;
}

.challenge-card {
  background: var(--md-code-bg-color);
  border: 2px solid transparent;
  border-radius: 15px;
  padding: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.challenge-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 5px;
  background: linear-gradient(90deg, var(--category-color), var(--category-color-light));
}

.challenge-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  border-color: var(--category-color);
}

.challenge-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 15px;
}

.challenge-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--md-default-fg-color);
  margin: 0 0 5px 0;
}

.challenge-event {
  font-size: 0.9rem;
  color: #888;
  font-style: italic;
}

.challenge-badges {
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: flex-end;
}

.difficulty-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.difficulty-easy {
  background: #d4edda;
  color: #155724;
}

.difficulty-medium {
  background: #fff3cd;
  color: #856404;
}

.difficulty-hard {
  background: #f8d7da;
  color: #721c24;
}

.category-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--category-color);
  color: white;
}

.challenge-description {
  font-size: 0.95rem;
  color: #666;
  line-height: 1.6;
  margin-bottom: 15px;
}

.challenge-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 15px;
  border-top: 1px solid rgba(102, 126, 234, 0.2);
}

.challenge-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.tag {
  padding: 3px 10px;
  background: rgba(102, 126, 234, 0.1);
  color: #667eea;
  border-radius: 10px;
  font-size: 0.8rem;
  font-weight: 500;
}

.challenge-date {
  font-size: 0.85rem;
  color: #888;
}

/* Category Colors */
.category-web { --category-color: #e74c3c; --category-color-light: #ff6b6b; }
.category-crypto { --category-color: #3498db; --category-color-light: #5dade2; }
.category-pwn { --category-color: #9b59b6; --category-color-light: #bb8fce; }
.category-reverse { --category-color: #f39c12; --category-color-light: #f8c471; }
.category-forensics { --category-color: #27ae60; --category-color-light: #58d68d; }
.category-misc { --category-color: #95a5a6; --category-color-light: #bdc3c7; }

/* No Results */
.no-results {
  text-align: center;
  padding: 60px 20px;
}

.no-results-icon {
  font-size: 4rem;
  margin-bottom: 20px;
  opacity: 0.5;
}

.no-results h3 {
  font-size: 1.5rem;
  color: #666;
  margin-bottom: 10px;
}

.no-results p {
  color: #999;
}

/* Dark Mode */
[data-md-color-scheme="slate"] .ctf-subtitle,
[data-md-color-scheme="slate"] .stat-label,
[data-md-color-scheme="slate"] .filter-group label,
[data-md-color-scheme="slate"] .challenge-description {
  color: #aaa;
}

[data-md-color-scheme="slate"] .difficulty-easy {
  background: rgba(46, 125, 50, 0.3);
  color: #81c784;
}

[data-md-color-scheme="slate"] .difficulty-medium {
  background: rgba(251, 140, 0, 0.3);
  color: #ffb74d;
}

[data-md-color-scheme="slate"] .difficulty-hard {
  background: rgba(211, 47, 47, 0.3);
  color: #e57373;
}

/* Responsive */
@media (max-width: 768px) {
  .ctf-header h1 {
    font-size: 2rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .filter-section {
    flex-direction: column;
  }

  .filter-group {
    width: 100%;
    flex-direction: column;
    align-items: stretch;
  }

  .filter-group select {
    width: 100%;
  }

  .challenges-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<script>
// CTF Challenges Data
const challenges = [
  {
    name: "SQL Injection Master",
    slug: "sql-injection-master",
    category: "web",
    difficulty: "medium",
    event: "HackTheBox 2024",
    description: "Tìm và khai thác SQL injection vulnerability để lấy flag từ database. Challenge này yêu cầu hiểu biết về SQL injection techniques và bypass filters.",
    tags: ["SQL", "Database", "Injection"],
    date: "2024-10-15",
    solved: true
  },
  {
    name: "Caesar Evolved",
    slug: "caesar-evolved",
    category: "crypto",
    difficulty: "easy",
    event: "picoCTF 2024",
    description: "Một biến thể nâng cao của Caesar cipher. Decrypt message để lấy flag. Perfect cho người mới bắt đầu học cryptography.",
    tags: ["Cipher", "Encryption", "Classical"],
    date: "2024-10-10",
    solved: true
  },
  {
    name: "Buffer Overflow Basic",
    slug: "buffer-overflow-basic",
    category: "pwn",
    difficulty: "easy",
    event: "PwnCollege",
    description: "Learn basic buffer overflow exploitation. Overflow the buffer để control return address và get shell access.",
    tags: ["Binary", "Exploitation", "Stack"],
    date: "2024-10-05",
    solved: true
  },
  {
    name: "Reverse Me If You Can",
    slug: "reverse-me-if-you-can",
    category: "reverse",
    difficulty: "hard",
    event: "DEFCON CTF 2024",
    description: "Reverse engineer một binary phức tạp với nhiều anti-debugging techniques. Cần phải hiểu assembly và debugging skills.",
    tags: ["Assembly", "Debugging", "IDA"],
    date: "2024-09-28",
    solved: true
  },
  {
    name: "Hidden in Plain Sight",
    slug: "hidden-in-plain-sight",
    category: "forensics",
    difficulty: "medium",
    event: "CyberDefenders",
    description: "Analyze network traffic PCAP file để tìm hidden data. Challenge này test khả năng phân tích network forensics.",
    tags: ["PCAP", "Wireshark", "Network"],
    date: "2024-09-20",
    solved: true
  },
  {
    name: "XSS Playground",
    slug: "xss-playground",
    category: "web",
    difficulty: "easy",
    event: "PortSwigger Academy",
    description: "Exploit XSS vulnerability để steal cookies và bypass WAF. Good introduction to client-side attacks.",
    tags: ["XSS", "JavaScript", "WAF Bypass"],
    date: "2024-09-15",
    solved: true
  },
  {
    name: "RSA Cryptanalysis",
    slug: "rsa-cryptanalysis",
    category: "crypto",
    difficulty: "hard",
    event: "CryptoHack",
    description: "Break weak RSA implementation với small exponent hoặc common modulus attack. Requires strong math background.",
    tags: ["RSA", "Number Theory", "Math"],
    date: "2024-09-10",
    solved: true
  },
  {
    name: "Return to Libc",
    slug: "return-to-libc",
    category: "pwn",
    difficulty: "medium",
    event: "pwnable.kr",
    description: "Bypass NX protection bằng return-to-libc technique. Chain các gadgets để execute system commands.",
    tags: ["ROP", "Binary", "NX Bypass"],
    date: "2024-09-05",
    solved: true
  },
  {
    name: "Steganography 101",
    slug: "steganography-101",
    category: "forensics",
    difficulty: "easy",
    event: "TryHackMe",
    description: "Extract hidden data từ image files. Learn about LSB steganography và các tools phổ biến.",
    tags: ["Stegano", "Images", "LSB"],
    date: "2024-08-30",
    solved: true
  },
  {
    name: "JWT Vulnerabilities",
    slug: "jwt-vulnerabilities",
    category: "web",
    difficulty: "medium",
    event: "HackTheBox",
    description: "Exploit JWT token vulnerabilities: algorithm confusion, weak secrets, và key injection attacks.",
    tags: ["JWT", "Authentication", "Tokens"],
    date: "2024-08-25",
    solved: true
  },
  {
    name: "Python Jail Break",
    slug: "python-jail-break",
    category: "misc",
    difficulty: "hard",
    event: "Google CTF 2024",
    description: "Escape từ restricted Python environment. Challenge này test creative thinking và Python internals knowledge.",
    tags: ["Python", "Sandbox", "Escape"],
    date: "2024-08-20",
    solved: true
  },
  {
    name: "Memory Dump Analysis",
    slug: "memory-dump-analysis",
    category: "forensics",
    difficulty: "hard",
    event: "SANS DFIR",
    description: "Analyze memory dump với Volatility để find malware artifacts, extract credentials, và reconstruct attack timeline.",
    tags: ["Memory", "Volatility", "Malware"],
    date: "2024-08-15",
    solved: true
  }
];

// Update stats
function updateStats() {
  const totalChallenges = challenges.length;
  const solvedChallenges = challenges.filter(c => c.solved).length;
  const easyCount = challenges.filter(c => c.difficulty === 'easy').length;
  const hardCount = challenges.filter(c => c.difficulty === 'hard').length;

  document.getElementById('total-challenges').textContent = totalChallenges;
  document.getElementById('solved-challenges').textContent = solvedChallenges;
  document.getElementById('easy-count').textContent = easyCount;
  document.getElementById('hard-count').textContent = hardCount;
}

// Create challenge card
function createChallengeCard(challenge) {
  const card = document.createElement('div');
  card.className = `challenge-card category-${challenge.category}`;
  
  const categoryNames = {
    web: 'Web',
    crypto: 'Crypto',
    pwn: 'Pwn',
    reverse: 'Reverse',
    forensics: 'Forensics',
    misc: 'Misc'
  };

  card.innerHTML = `
    <div class="challenge-header">
      <div>
        <h3 class="challenge-title">${challenge.name}</h3>
        <div class="challenge-event">${challenge.event}</div>
      </div>
      <div class="challenge-badges">
        <span class="difficulty-badge difficulty-${challenge.difficulty}">${challenge.difficulty}</span>
        <span class="category-badge">${categoryNames[challenge.category]}</span>
      </div>
    </div>
    <p class="challenge-description">${challenge.description}</p>
    <div class="challenge-footer">
      <div class="challenge-tags">
        ${challenge.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
      </div>
      <div class="challenge-date">${formatDate(challenge.date)}</div>
    </div>
  `;

  card.addEventListener('click', () => {
    window.location.href = `${challenge.slug}/`;
  });

  return card;
}

// Format date
function formatDate(dateStr) {
  const date = new Date(dateStr);
  const options = { year: 'numeric', month: 'short', day: 'numeric' };
  return date.toLocaleDateString('en-US', options);
}

// Filter and sort challenges
function filterAndSortChallenges() {
  const searchTerm = document.getElementById('ctf-search').value.toLowerCase();
  const categoryFilter = document.getElementById('category-filter').value;
  const difficultyFilter = document.getElementById('difficulty-filter').value;
  const sortBy = document.getElementById('sort-by').value;

  let filtered = challenges.filter(challenge => {
    const matchesSearch = challenge.name.toLowerCase().includes(searchTerm) ||
                         challenge.description.toLowerCase().includes(searchTerm) ||
                         challenge.tags.some(tag => tag.toLowerCase().includes(searchTerm));
    const matchesCategory = categoryFilter === 'all' || challenge.category === categoryFilter;
    const matchesDifficulty = difficultyFilter === 'all' || challenge.difficulty === difficultyFilter;
    
    return matchesSearch && matchesCategory && matchesDifficulty;
  });

  // Sort
  filtered.sort((a, b) => {
    switch(sortBy) {
      case 'date-desc':
        return new Date(b.date) - new Date(a.date);
      case 'date-asc':
        return new Date(a.date) - new Date(b.date);
      case 'name-asc':
        return a.name.localeCompare(b.name);
      case 'name-desc':
        return b.name.localeCompare(a.name);
      case 'difficulty':
        const diffOrder = { easy: 1, medium: 2, hard: 3 };
        return diffOrder[a.difficulty] - diffOrder[b.difficulty];
      default:
        return 0;
    }
  });

  renderChallenges(filtered);
}

// Render challenges
function renderChallenges(challengesToRender) {
  const grid = document.getElementById('challenges-grid');
  const noResults = document.getElementById('no-results');
  
  grid.innerHTML = '';
  
  if (challengesToRender.length === 0) {
    grid.style.display = 'none';
    noResults.style.display = 'block';
  } else {
    grid.style.display = 'grid';
    noResults.style.display = 'none';
    challengesToRender.forEach(challenge => {
      grid.appendChild(createChallengeCard(challenge));
    });
  }
}

// Initialize
function init() {
  updateStats();
  renderChallenges(challenges);

  // Event listeners
  document.getElementById('ctf-search').addEventListener('input', filterAndSortChallenges);
  document.getElementById('category-filter').addEventListener('change', filterAndSortChallenges);
  document.getElementById('difficulty-filter').addEventListener('change', filterAndSortChallenges);
  document.getElementById('sort-by').addEventListener('change', filterAndSortChallenges);
}

// Run when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
</script>
