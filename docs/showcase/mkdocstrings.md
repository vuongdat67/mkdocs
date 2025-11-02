# mkdocstrings

**Automatic documentation from sources, for MkDocs.**

mkdocstrings is a plugin for MkDocs that allows you to generate API documentation from your source code.

## Features

- 🔍 **Auto-discovery** - Automatically find and document your code
- 🎨 **Themeable** - Works seamlessly with Material for MkDocs
- 🐍 **Multi-language** - Support for Python, and more via handlers
- 📝 **Cross-references** - Automatic linking between documented items
- ⚙️ **Customizable** - Fine-tune what gets documented

## Installation

```bash
pip install mkdocstrings[python]
```

## Configuration

Add to your `mkdocs.yml`:

```yaml
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          options:
            docstring_style: google
            show_source: true
```

## Usage

### Basic Example

Simply use the `:::` syntax in your markdown:

```markdown
# API Reference

::: mypackage.mymodule
```

### Advanced Configuration

```markdown
::: mypackage.MyClass
    options:
      show_root_heading: true
      show_source: true
      members:
        - method1
        - method2
      filters:
        - "!^_"
```

## Docstring Styles

mkdocstrings supports multiple docstring formats:

=== "Google Style"
    ```python
    def function(arg1: str, arg2: int) -> bool:
        """Summary line.
        
        Extended description.
        
        Args:
            arg1: Description of arg1.
            arg2: Description of arg2.
            
        Returns:
            Description of return value.
        """
        return True
    ```

=== "NumPy Style"
    ```python
    def function(arg1, arg2):
        """Summary line.
        
        Parameters
        ----------
        arg1 : str
            Description of arg1.
        arg2 : int
            Description of arg2.
            
        Returns
        -------
        bool
            Description of return value.
        """
        return True
    ```

=== "Sphinx Style"
    ```python
    def function(arg1, arg2):
        """Summary line.
        
        :param arg1: Description of arg1.
        :type arg1: str
        :param arg2: Description of arg2.
        :type arg2: int
        :return: Description of return value.
        :rtype: bool
        """
        return True
    ```

## Cross-References

Automatically create links to other documented items:

```markdown
See [`MyClass.method`][mypackage.MyClass.method] for details.
```

## Handlers

mkdocstrings uses handlers for different languages:

- **Python** - Full support via griffe
- **Crystal** - Via crystal handler
- **VBA** - Via vba handler

## Example Output

The generated documentation includes:

- ✅ Function/method signatures
- ✅ Parameter descriptions
- ✅ Return type information
- ✅ Examples from docstrings
- ✅ Source code (optional)
- ✅ Cross-references

## Integration with Material Theme

Works perfectly with Material for MkDocs features:

- Code annotations
- Tabbed content
- Admonitions
- Dark mode

## Links

- 📚 [Documentation](https://mkdocstrings.github.io/)
- 🐙 [GitHub Repository](https://github.com/mkdocstrings/mkdocstrings)
- 📦 [PyPI Package](https://pypi.org/project/mkdocstrings/)
