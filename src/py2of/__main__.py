"""Command-line interface."""
import sys
from importlib import import_module
from pathlib import Path

import click

from py2of.service.case_dumper import CaseDumper


@click.group()
@click.version_option()
def main() -> None:
    """Ultimate PyFoam!!!."""


@main.command()
@click.argument("content_file", default="case")
@click.argument("dump_dir", default="of_case")
def dump(content_file: Path, dump_dir: Path) -> None:
    sys.path.append("")
    CaseDumper(import_module(str(content_file)).case).dump(dump_dir)
    sys.path.pop()


if __name__ == "__main__":
    main(prog_name="py2of")  # pragma: no cover
