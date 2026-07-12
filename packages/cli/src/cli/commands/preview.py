import typer
from rich.console import Console

app = typer.Typer(help="Preview a component")
console = Console()


@app.callback(invoke_without_command=True)
def preview_component(component: str = typer.Argument(...)):
    console.print(f"Opening preview for [bold]{component}[/bold]...")
