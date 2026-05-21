from pathlib import Path

import typer
from rich import print

from amnay.core.engine import ValidationEngine
from amnay.core.registry import PROVIDERS


from amnay.core.policy_loader import (
    PolicyLoader,
)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_POLICY = BASE_DIR / "policies/default.yaml"

app = typer.Typer()

SEVERITY_COLORS = {
    "info": "blue",
    "low": "cyan",
    "medium": "yellow",
    "high": "magenta",
    "critical": "red",
}


@app.callback()
def callback():
    """
    Amnay CI validation engine
    """
    pass


@app.command()
def validate(
    provider: str,
    file: str,
    policy: str = DEFAULT_POLICY,
):

    if provider not in PROVIDERS:

        print(f"[red]Unknown provider: {provider}[/red]")

        raise typer.Exit(code=1)

    workflow = PROVIDERS[provider].load(file)

    policy_data = PolicyLoader.load(policy)

    engine = ValidationEngine(policy_data)

    errors = engine.validate(workflow)

    if errors:

        for error in errors:
            color = SEVERITY_COLORS.get(error.severity, "white")

            print(
                f"[{color}]"
                f"\\[{error.severity}] "
                f"{error.rule_id}: "
                f"{error.message}"
                f"[/{color}]"
            )

        raise typer.Exit(code=1)

    print("[green]Validation passed[/green]")


if __name__ == "__main__":
    app()
