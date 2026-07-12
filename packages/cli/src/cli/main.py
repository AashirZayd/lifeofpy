import typer
from .commands import init, add, search, info, preview

app = typer.Typer(help="LifeOfPy Ecosystem CLI")

app.add_typer(init.app, name="init")
app.add_typer(add.app, name="add")
app.add_typer(search.app, name="search")
app.add_typer(info.app, name="info")
app.add_typer(preview.app, name="preview")

if __name__ == "__main__":
    app()
