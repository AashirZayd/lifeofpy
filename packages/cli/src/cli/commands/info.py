import typer
from rich.console import Console

app = typer.Typer(help="Get component info")
console = Console()


@app.callback(invoke_without_command=True)
def info_component(component: str = typer.Argument(...)):
    console.print(f"Fetching info for [bold]{component}[/bold]...")
