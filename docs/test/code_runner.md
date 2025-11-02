---
title: Python Code Runner
---

# 🐍 Python Code Runner

Chạy Python code trực tiếp trong browser - không cần server!

---

## 🎮 Live Python Editor

Gõ code vào editor bên dưới và nhấn **Run** để xem kết quả:

<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">🐍 Python Interactive Editor</span>
    <button class="run-btn" onclick="runPythonCode()">▶ Run Code</button>
  </div>
  
  <textarea id="python-code" class="code-editor" spellcheck="false">
# Viết Python code của bạn ở đây
print("Hello from Python in Browser! 🚀")

# Tính toán đơn giản
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# In ra 10 số Fibonacci đầu tiên
print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
</textarea>
  
  <div class="output-section">
    <div class="output-header">
      <span>📤 Output:</span>
      <button class="clear-btn" onclick="document.getElementById('python-output').innerHTML=''">Clear</button>
    </div>
    <pre id="python-output" class="output-area">Nhấn 'Run Code' để xem kết quả...</pre>
  </div>
</div>

---

## 📝 Examples

### Example 1: Hello World

<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">Example 1: Basics</span>
    <button class="run-btn" onclick="runCode('code1', 'output1')">▶ Run</button>
  </div>
  
  <textarea id="code1" class="code-editor" spellcheck="false">
# Variables and types
name = "Dat"
age = 25
pi = 3.14159

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Pi: {pi:.2f}")

# List operations
fruits = ["apple", "banana", "cherry"]
print(f"\nFruits: {fruits}")
fruits.append("orange")
print(f"After append: {fruits}")
</textarea>
  
  <div class="output-section">
    <div class="output-header">
      <span>📤 Output:</span>
      <button class="clear-btn" onclick="document.getElementById('output1').innerHTML=''">Clear</button>
    </div>
    <pre id="output1" class="output-area">Nhấn Run để xem kết quả...</pre>
  </div>
</div>

### Example 2: Functions & Loops

<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">Example 2: Functions</span>
    <button class="run-btn" onclick="runCode('code2', 'output2')">▶ Run</button>
  </div>
  
  <textarea id="code2" class="code-editor" spellcheck="false">
# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find prime numbers
primes = [x for x in range(2, 50) if is_prime(x)]
print(f"Prime numbers < 50: {primes}")
print(f"Total primes: {len(primes)}")
</textarea>
  
  <div class="output-section">
    <div class="output-header">
      <span>📤 Output:</span>
      <button class="clear-btn" onclick="document.getElementById('output2').innerHTML=''">Clear</button>
    </div>
    <pre id="output2" class="output-area">Nhấn Run để xem kết quả...</pre>
  </div>
</div>

### Example 3: Data Structures

<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">Example 3: Dictionary & List Comprehension</span>
    <button class="run-btn" onclick="runCode('code3', 'output3')">▶ Run</button>
  </div>
  
  <textarea id="code3" class="code-editor" spellcheck="false">
# Student grades
students = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Charlie": [75, 80, 85]
}

# Calculate average
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    print(f"{name}: grades={grades}, average={avg:.2f}")

# List comprehension
squares = [x**2 for x in range(1, 11)]
print(f"\nSquares: {squares}")

evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")
</textarea>
  
  <div class="output-section">
    <div class="output-header">
      <span>📤 Output:</span>
      <button class="clear-btn" onclick="document.getElementById('output3').innerHTML=''">Clear</button>
    </div>
    <pre id="output3" class="output-area">Nhấn Run để xem kết quả...</pre>
  </div>
</div>

---

## 🔧 Cách sử dụng trong file .md khác

### Cách 1: Copy Full Component (Recommended)

Copy đoạn code này vào bất kỳ file `.md` nào:

````markdown
<div class="python-runner">
  <div class="runner-header">
    <span class="runner-title">🐍 Python Code</span>
    <button class="run-btn" onclick="runCode('mycode', 'myoutput')">▶ Run</button>
  </div>
  
  <textarea id="mycode" class="code-editor" spellcheck="false">
# Your Python code here
print("Hello World!")
</textarea>
  
  <div class="output-section">
    <div class="output-header">📤 Output:</div>
    <pre id="myoutput" class="output-area">Click Run...</pre>
  </div>
</div>
````

!!! warning "Important"
    - Mỗi code runner phải có **ID duy nhất** (`mycode`, `myoutput`)
    - Nếu có nhiều runners trong 1 page, đổi ID: `code1/output1`, `code2/output2`, etc.

### Cách 2: Simple Inline (Minimal)

Nếu chỉ cần 1 runner đơn giản:

````markdown
<div class="python-runner">
  <textarea id="code" class="code-editor" spellcheck="false">
print("Quick Python code here!")
</textarea>
  <button class="run-btn" onclick="runCode('code', 'output')">▶ Run</button>
  <pre id="output" class="output-area"></pre>
</div>
````

---

## 🎨 Features

✨ **Syntax Highlighting** - Code editor với font monospace  
⚡ **Instant Execution** - Chạy ngay trong browser  
🎯 **Multiple Runners** - Nhiều code blocks trong 1 trang  
📱 **Responsive** - Hoạt động tốt trên mobile  
🌙 **Dark Mode** - Tự động theo theme  
🔒 **Safe** - Chạy sandboxed trong browser  

---

## ⚠️ Limitations

!!! info "Lưu ý"
    - ❌ Không dùng được thư viện ngoài (numpy, pandas, etc.) - chỉ có built-in Python
    - ❌ Không có file I/O (không đọc/ghi file)
    - ❌ Không có network requests
    - ✅ Perfect cho: học thuật toán, logic, data structures
    - ✅ Đủ dùng cho: loops, functions, OOP basics, list comprehension

---

## 💡 Tips

!!! tip "Best Practices"
    1. **Keep code simple** - Tránh code quá phức tạp
    2. **Use print()** - Để xem output
    3. **Multiple runners** - Tách thành nhiều examples nhỏ
    4. **Error handling** - Code sẽ show error nếu có lỗi

---

<!-- Pyodide CDN -->
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

/* Status indicator */
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
    console.log("✅ Pyodide loaded");
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
    outputElement.textContent = "⏳ Loading Python environment...";
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

function runPythonCode() {
  runCode('python-code', 'python-output');
}

function clearOutput(outputId = 'python-output') {
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
