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
@click.argument("content_file", type=click.Path(exists=True, path_type=Path))
@click.option("--dump-dir", default="of_case", type=click.Path(path_type=Path))
@click.option("--case-mod-attr", default="case")
def dump(content_file: Path, dump_dir: Path, case_mod_attr: str) -> None:
    sys.path.insert(0, str(content_file.parent))
    module = import_module(content_file.stem)
    CaseDumper(getattr(module, case_mod_attr)).dump(dump_dir)
    del sys.path[0]


if __name__ == "__main__":
    main(prog_name="py2of")  # pragma: no cover
