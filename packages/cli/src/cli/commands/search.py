import typer
from rich.console import Console

app = typer.Typer(help="Search the registry")
console = Console()


@app.callback(invoke_without_command=True)
def search_components(query: str = typer.Argument(..., help="Search query")):
    console.print(f"Searching for [bold]{query}[/bold]...")
