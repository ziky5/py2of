"""Command-line interface."""
import sys
from importlib import import_module
from pathlib import Path
from typing import Any

import click

from py2of.service.case_dumper import CaseDumper


class ImportModule:
    def __init__(self, path: Path) -> None:
        self.path = path

    def __enter__(self) -> Any:
        sys.path.insert(0, str(self.path.parent))
        return import_module(self.path.stem)

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        del sys.path[0]


@click.group()
@click.version_option()
@click.option(
    "--log",
    type=click.Choice(["debug", "info", "warning", "error"], case_sensitive=False),
    help="Sets logging level.",
    default="info",
    show_default=True,
)
@click.option(
    "--logging-yaml",
    type=click.Path(exists=True),
    default=None,
    help="Path to alternative logging yaml to be used.",
)
def main(log: str, logging_yaml: str | Path) -> None:
    """Ultimate PyFoam!!!."""


@main.command()
@click.argument("content_file", type=click.Path(exists=True, path_type=Path))
@click.option("--dump-dir", default="of_case", type=click.Path(path_type=Path))
@click.option("--case-mod-attr", default="case")
def dump(content_file: Path, dump_dir: Path, case_mod_attr: str) -> None:
    with ImportModule(content_file) as module:
        CaseDumper(getattr(module, case_mod_attr)).dump(dump_dir)


if __name__ == "__main__":
    main(prog_name="py2of")  # pragma: no cover
