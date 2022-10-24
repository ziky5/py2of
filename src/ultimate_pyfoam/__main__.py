"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Ultimate PyFoam!!!."""


if __name__ == "__main__":
    main(prog_name="ultimate-pyfoam")  # pragma: no cover
