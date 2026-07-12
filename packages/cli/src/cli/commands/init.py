import typer
from rich.console import Console

app = typer.Typer(help="Initialize a new project")
console = Console()


@app.callback(invoke_without_command=True)
def init_project():
    console.print("[bold green]Initializing LifeOfPy configuration...[/bold green]")
