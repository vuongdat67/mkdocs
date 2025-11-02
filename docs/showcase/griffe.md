# griffe

**Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API.**

## Overview

Griffe is a Python library that extracts and analyzes the structure of Python codebases. It's the engine behind mkdocstrings and can be used independently for various purposes.

## Features

- 🔍 **Static Analysis** - Parse code without executing it
- 🌳 **AST-based** - Uses Python's Abstract Syntax Tree
- 🎯 **Type Annotations** - Full support for type hints
- 📊 **API Breakage Detection** - Find breaking changes between versions
- ⚡ **Fast** - Efficient parsing and traversal

## Installation

```bash
pip install griffe
```

## Command Line Usage

### Dump API as JSON

```bash
griffe dump mypackage
```

Output:

```json
{
  "name": "mypackage",
  "kind": "module",
  "members": {
    "MyClass": {
      "kind": "class",
      "docstring": "A sample class.",
      "members": {
        "method": {
          "kind": "function",
          "parameters": [...],
          "returns": "str"
        }
      }
    }
  }
}
```

### Check for Breaking Changes

```bash
griffe check mypackage --against 1.0.0
```

Output will show:

- Removed members
- Changed signatures
- Modified return types

## Python API

### Load and Inspect

```python
from griffe import GriffeLoader

loader = GriffeLoader()
module = loader.load_module("mypackage")

# Iterate through classes
for name, cls in module.classes.items():
    print(f"Class: {name}")
    
    # Check methods
    for method_name, method in cls.functions.items():
        print(f"  Method: {method_name}")
        print(f"    Parameters: {method.parameters}")
        print(f"    Returns: {method.returns}")
```

### Access Docstrings

```python
# Get parsed docstring
docstring = module["MyClass"].docstring

print(f"Summary: {docstring.value}")
print(f"Parameters: {docstring.parameters}")
print(f"Returns: {docstring.returns}")
```

### Check API Changes

```python
from griffe import load, temporary_visited_module

old = load("mypackage")  # Current version

with temporary_visited_module("mypackage") as tmp:
    # Install and load old version
    new = load("mypackage")
    
    # Compare
    breakages = old.compare(new)
    
    for breakage in breakages:
        print(f"{breakage.kind}: {breakage.name}")
```

## Data Model

Griffe represents code with these main objects:

### Module

```python
module.name          # Module name
module.filepath      # Path to file
module.members       # Dict of members
module.exports       # Exported names
```

### Class

```python
cls.bases            # Base classes
cls.decorators       # Class decorators
cls.functions        # Methods
cls.attributes       # Class attributes
```

### Function

```python
func.parameters      # Parameter list
func.returns         # Return annotation
func.decorators      # Decorators
func.docstring       # Parsed docstring
```

## Use Cases

### 1. Generate Documentation

Extract structure for documentation generators:

```python
loader = GriffeLoader()
api = loader.load_module("mypackage")

for obj in api.members.values():
    render_documentation(obj)
```

### 2. API Breaking Change Detection

In CI/CD pipelines:

```bash
# In your CI script
griffe check mypackage --against origin/main
```

### 3. Code Analysis

Analyze code quality and structure:

```python
# Find all async functions
async_funcs = [
    func for func in module.all_functions
    if func.is_async
]

# Find classes without docstrings
undocumented = [
    cls for cls in module.classes.values()
    if not cls.docstring
]
```

## Performance

Griffe is designed for speed:

- ⚡ **Parallel loading** - Load multiple modules concurrently
- 🎯 **Lazy evaluation** - Only parse what you need
- 💾 **Caching** - Cache parsed results

## Integration

Griffe is used by:

- **mkdocstrings** - Documentation generation
- **API diff tools** - Breaking change detection
- **Type checkers** - Static analysis tools

## Links

- 📚 [Documentation](https://mkdocstrings.github.io/griffe/)
- 🐙 [GitHub Repository](https://github.com/mkdocstrings/griffe)
- 📦 [PyPI Package](https://pypi.org/project/griffe/)
