# Tips for Writing Good Python CLI Libraries

Building user-friendly command-line interfaces requires thoughtful design. Here are my best tips!

## 1. Use Click or Typer

Don't reinvent the wheel. Use modern CLI frameworks.

=== "Click"
    ```python
    import click

    @click.command()
    @click.option('--name', prompt='Your name',
                  help='The person to greet.')
    def hello(name):
        """Simple program that greets NAME."""
        click.echo(f'Hello {name}!')
    ```

=== "Typer"
    ```python
    import typer

    def main(name: str = typer.Option(..., prompt=True)):
        """Simple program that greets NAME."""
        typer.echo(f'Hello {name}!')
    
    if __name__ == "__main__":
        typer.run(main)
    ```

## 2. Provide Good Help Text

Your help text is your documentation!

```python
@click.command()
@click.option(
    '--config', '-c',
    type=click.Path(exists=True),
    help='Path to configuration file. Defaults to ~/.myapp/config.yml'
)
@click.option(
    '--verbose', '-v',
    count=True,
    help='Increase verbosity. Use -vv for debug mode.'
)
def deploy(config, verbose):
    """Deploy your application to production.
    
    This command will:
    - Validate configuration
    - Build Docker images
    - Push to registry
    - Update Kubernetes manifests
    """
    pass
```

## 3. Use Progress Bars

Show progress for long-running operations.

```python
import click

def process_files(files):
    with click.progressbar(files, label='Processing') as bar:
        for file in bar:
            # Process file
            time.sleep(0.1)
```

## 4. Colored Output

Make your CLI visually appealing!

```python
import click

click.secho('Success!', fg='green', bold=True)
click.secho('Warning!', fg='yellow')
click.secho('Error!', fg='red', bold=True)
```

## 5. Confirmation Prompts

Protect users from destructive actions.

```python
@click.command()
@click.option('--yes', '-y', is_flag=True, 
              help='Skip confirmation')
def delete_all(yes):
    """Delete all data (DANGEROUS!)"""
    if not yes:
        click.confirm('Are you sure?', abort=True)
    
    click.echo('Deleting...')
```

## 6. Environment Variables

Support configuration via environment variables.

```python
@click.command()
@click.option(
    '--api-key',
    envvar='MY_API_KEY',
    required=True,
    help='API key (can be set via MY_API_KEY env var)'
)
def connect(api_key):
    """Connect to the API."""
    pass
```

## 7. Subcommands

Organize complex CLIs with subcommands.

```python
@click.group()
def cli():
    """My awesome CLI tool."""
    pass

@cli.command()
def init():
    """Initialize the project."""
    click.echo('Initializing...')

@cli.command()
def deploy():
    """Deploy the project."""
    click.echo('Deploying...')

if __name__ == '__main__':
    cli()
```

## 8. Rich Output

Use `rich` for beautiful terminal output!

```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Server Status")
table.add_column("Server", style="cyan")
table.add_column("Status", style="magenta")

table.add_row("prod-1", "[green]Online[/green]")
table.add_row("prod-2", "[red]Offline[/red]")

console.print(table)
```

## Best Practices Checklist

- [x] Clear, descriptive command names
- [x] Comprehensive help text
- [x] Support for `--version` flag
- [x] Sensible defaults
- [x] Progress indicators for long operations
- [x] Colored output for clarity
- [x] Confirmation for destructive actions
- [x] Environment variable support
- [x] Exit codes (0 for success, non-zero for errors)

## Example: Complete CLI

```python
import click
from rich.console import Console

console = Console()

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """MyApp - A fantastic CLI tool!"""
    pass

@cli.command()
@click.argument('name')
def greet(name):
    """Greet someone nicely."""
    console.print(f"[green]Hello, {name}! 👋[/green]")

@cli.command()
@click.option('--count', default=1, help='Number of greetings')
@click.option('--name', prompt='Your name')
def hello(count, name):
    """Say hello multiple times."""
    for _ in range(count):
        console.print(f"Hello {name}!")

if __name__ == '__main__':
    cli()
```

## Conclusion

Building great CLIs is about **empathy** for your users. Make it intuitive, helpful, and beautiful! ✨
