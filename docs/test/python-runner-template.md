---
title: Python Runner Template
---

# Template: Python Code Runner

Copy các template dưới đây vào file `.md` của bạn để có Python code runner!

---

## 📋 Template 1: Full Featured Runner

Copy toàn bộ đoạn này:

```html
<!-- Python Code Runner - Full Featured -->
<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">🐍 Python Interactive Editor</span>
    <button class="run-btn" onclick="runCode('mycode1', 'myoutput1')">▶ Run Code</button>
  </div>
  
  <textarea id="mycode1" class="code-editor" spellcheck="false">
# Write your Python code here
print("Hello, World!")

# Example: Calculate factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(f"5! = {factorial(5)}")
</textarea>
  
  <div class="output-section">
    <div class="output-header">
      <span>📤 Output:</span>
      <button class="clear-btn" onclick="clearOutput('myoutput1')">Clear</button>
    </div>
    <pre id="myoutput1" class="output-area">Click 'Run Code' to see results...</pre>
  </div>
</div>
```

---

## 📋 Template 2: Minimal Runner

Nếu muốn đơn giản hơn:

```html
<!-- Python Code Runner - Minimal -->
<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">🐍 Python Code</span>
    <button class="run-btn" onclick="runCode('code2', 'output2')">▶ Run</button>
  </div>
  
  <textarea id="code2" class="code-editor" spellcheck="false">
print("Quick Python test!")
</textarea>
  
  <div class="output-section">
    <div class="output-header">📤 Output:</div>
    <pre id="output2" class="output-area">Click Run...</pre>
  </div>
</div>
```

---

## 📋 Template 3: Multiple Runners

Nếu cần nhiều runners trong 1 page, đổi ID cho từng cái:

```html
<!-- Runner #1 -->
<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">Example 1: Basics</span>
    <button class="run-btn" onclick="runCode('codeA', 'outputA')">▶ Run</button>
  </div>
  <textarea id="codeA" class="code-editor" spellcheck="false">
print("Runner A")
</textarea>
  <div class="output-section">
    <div class="output-header">📤 Output:</div>
    <pre id="outputA" class="output-area">...</pre>
  </div>
</div>

<!-- Runner #2 -->
<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">Example 2: Advanced</span>
    <button class="run-btn" onclick="runCode('codeB', 'outputB')">▶ Run</button>
  </div>
  <textarea id="codeB" class="code-editor" spellcheck="false">
print("Runner B")
</textarea>
  <div class="output-section">
    <div class="output-header">📤 Output:</div>
    <pre id="outputB" class="output-area">...</pre>
  </div>
</div>
```

---

## 🔧 Required Scripts

**QUAN TRỌNG**: Thêm đoạn này vào **CUỐI FILE** `.md` (chỉ cần thêm 1 lần):

```html
<!-- Pyodide Script -->
<script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>

<style>
/* Container */
.python-runner {
  margin: 30px 0;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 4px;
  overflow: hidden;
  background: var(--md-code-bg-color);
}

/* Header */
.runner-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: var(--md-code-bg-color);
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}

.runner-title {
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--md-default-fg-color);
}

/* Buttons */
.run-btn {
  background: var(--md-primary-fg-color);
  color: white;
  border: none;
  padding: 8px 20px;
  border-radius: 4px;
  font-weight: 500;
  font-size: 0.9rem;
  cursor: pointer;
  transition: opacity 0.2s;
}

.run-btn:hover {
  opacity: 0.85;
}

.run-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.clear-btn {
  background: transparent;
  color: var(--md-default-fg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
}

.clear-btn:hover {
  background: var(--md-default-fg-color--lightest);
}

/* Code Editor */
.code-editor {
  width: 100%;
  min-height: 200px;
  padding: 15px;
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
  font-size: 14px;
  line-height: 1.5;
  background: var(--md-code-bg-color);
  color: var(--md-code-fg-color);
  border: none;
  resize: vertical;
  outline: none;
  tab-size: 4;
}

/* Output Section */
.output-section {
  border-top: 1px solid var(--md-default-fg-color--lightest);
}

.output-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  background: var(--md-code-bg-color);
  font-weight: 600;
  font-size: 0.9rem;
  color: var(--md-default-fg-color);
}

.output-area {
  margin: 0;
  padding: 15px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 13px;
  line-height: 1.6;
  white-space: pre-wrap;
  word-wrap: break-word;
  max-height: 400px;
  overflow-y: auto;
  min-height: 100px;
}

/* Dark mode */
[data-md-color-scheme="slate"] .code-editor {
  background: #1e1e1e;
  color: #d4d4d4;
}

[data-md-color-scheme="slate"] .output-area {
  background: #0d1117;
  color: #c9d1d9;
}

/* Mobile */
@media (max-width: 768px) {
  .runner-header {
    flex-direction: column;
    gap: 10px;
    align-items: stretch;
  }
  .run-btn {
    width: 100%;
  }
}

/* Loading spinner */
.loading-spinner {
  display: inline-block;
  width: 14px;
  height: 14px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>

<script>
let pyodideReady = false;
let pyodide = null;

async function initPyodide() {
  if (pyodideReady) return;
  try {
    pyodide = await loadPyodide({
      indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
    });
    pyodideReady = true;
    console.log("✅ Pyodide ready");
  } catch (error) {
    console.error("❌ Pyodide error:", error);
  }
}

async function runCode(codeId, outputId) {
  const codeElement = document.getElementById(codeId);
  const outputElement = document.getElementById(outputId);
  
  if (!codeElement || !outputElement) return;
  
  const code = codeElement.value.trim();
  if (!code) {
    outputElement.textContent = "No code to run.";
    return;
  }
  
  if (!pyodideReady) {
    outputElement.textContent = "⏳ Loading Python...";
    await initPyodide();
  }
  
  outputElement.textContent = "⏳ Running...";
  
  try {
    await pyodide.runPythonAsync(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
    `);
    
    await pyodide.runPythonAsync(code);
    
    const stdout = await pyodide.runPythonAsync("sys.stdout.getvalue()");
    const stderr = await pyodide.runPythonAsync("sys.stderr.getvalue()");
    
    if (stderr) {
      outputElement.textContent = stderr;
      outputElement.style.color = "#dc3545";
    } else if (stdout) {
      outputElement.textContent = stdout;
      outputElement.style.color = "var(--md-code-fg-color)";
    } else {
      outputElement.textContent = "✓ Code executed (no output)";
      outputElement.style.color = "#4caf50";
    }
  } catch (error) {
    outputElement.textContent = `Error: ${error.message}`;
    outputElement.style.color = "#dc3545";
  }
}

function clearOutput(outputId) {
  const outputElement = document.getElementById(outputId);
  if (outputElement) {
    outputElement.textContent = "Output cleared.";
    outputElement.style.color = "var(--md-default-fg-color)";
  }
}

// Auto-init
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPyodide);
} else {
  initPyodide();
}
</script>
```

---

## ✅ Checklist khi sử dụng

- [ ] Copy template HTML vào vị trí mong muốn
- [ ] Đổi ID cho unique: `mycode1`, `myoutput1`, etc.
- [ ] Thêm scripts vào cuối file (chỉ 1 lần)
- [ ] Test bằng cách nhấn Run

---

## 🎯 Quick Start

### Bước 1: Copy HTML

Copy template bạn muốn (Full Featured hoặc Minimal)

### Bước 2: Paste vào .md file

```markdown
---
title: My Python Tutorial
---

# Python Tutorial

Học Python qua examples:

<!-- Paste template ở đây -->
<div class="python-runner">
  ...
</div>

More content...

<!-- Scripts ở cuối file -->
<script src="..."></script>
<style>...</style>
<script>...</script>
```

### Bước 3: Customize

Thay đổi:
- `runner-title` - Tiêu đề
- Code mặc định trong `<textarea>`
- ID nếu có nhiều runners

### Bước 4: Done! 🎉

Save và xem trang, nhấn Run để test!

---

## 💡 Tips

!!! tip "Pro Tips"
    - **Preload code**: Để sẵn code example trong textarea
    - **Multiple examples**: Tạo nhiều runners cho từng concept
    - **Error handling**: Code tự động show error message
    - **Mobile friendly**: Responsive design tự động

!!! warning "Limitations"
    - Chỉ có Python standard library
    - Không có numpy, pandas, matplotlib
    - Không có file I/O
    - Perfect cho: algorithms, data structures, logic

---

## 🔗 Related

- [Full Demo Page](code_runner.md) - Xem examples đầy đủ
- [Python Tutorial](../programming/python/) - Học Python
- [Mermaid Guide](../programming/mermaid-guide.md) - Vẽ diagrams

---

**Happy Coding! 🚀**
