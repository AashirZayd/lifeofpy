import typer
from rich.console import Console

app = typer.Typer(help="Add a component to your project")
console = Console()


@app.callback(invoke_without_command=True)
def add_component(component: str = typer.Argument(..., help="Component ID to add")):
    console.print(f"[bold blue]Fetching {component} from the registry...[/bold blue]")
