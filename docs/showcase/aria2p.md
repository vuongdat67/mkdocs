# aria2p

**aria2p** is a command-line tool and Python library to interact with an `aria2c` daemon process through JSON-RPC.

## Features

- 🚀 **Fast downloads** - Leverage aria2's multi-connection downloading
- 🎨 **Beautiful TUI** - Terminal user interface for monitoring downloads
- 🐍 **Python API** - Full-featured Python library
- 📊 **Statistics** - Real-time download statistics and progress

## Installation

```bash
pip install aria2p
```

## Quick Start

### Command Line

```bash
# Start the TUI
aria2p

# Add a download
aria2p add "https://example.com/file.zip"

# List downloads
aria2p list

# Pause all downloads
aria2p pause-all
```

### Python API

```python
import aria2p

# Create API instance
aria2 = aria2p.API(
    aria2p.Client(
        host="http://localhost",
        port=6800,
        secret=""
    )
)

# Add download
download = aria2.add_uris(["https://example.com/file.zip"])

# Get download status
print(f"Status: {download.status}")
print(f"Progress: {download.progress}%")
print(f"Speed: {download.download_speed} B/s")
```

## TUI Interface

The terminal user interface provides:

- **Real-time monitoring** of all downloads
- **Keyboard shortcuts** for quick actions
- **Sorting and filtering** capabilities
- **Detailed information** for each download

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `a` | Add download |
| `p` | Pause/Resume |
| `r` | Remove download |
| `q` | Quit |

## Configuration

Create a config file at `~/.config/aria2p/config.yml`:

```yaml
host: localhost
port: 6800
secret: your-secret-token
```

## Advanced Usage

### Batch Downloads

```python
urls = [
    "https://example.com/file1.zip",
    "https://example.com/file2.zip",
    "https://example.com/file3.zip",
]

downloads = aria2.add_uris(urls)
```

### Custom Options

```python
options = {
    "dir": "/downloads",
    "max-download-limit": "1M",
    "split": "10"
}

download = aria2.add_uris(
    ["https://example.com/file.zip"],
    options=options
)
```

## Links

- 📚 [Documentation](https://pawamoy.github.io/aria2p/)
- 🐙 [GitHub Repository](https://github.com/pawamoy/aria2p)
- 📦 [PyPI Package](https://pypi.org/project/aria2p/)
