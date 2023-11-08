from collections import UserDict
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from textwrap import indent
from typing import Any
from typing import Collection
import logging

from py2of.domain.dimensions import Dimensions
from py2of.domain.of_list import OfList, NonUniformList, UniformList

logger = logging.getLogger(__name__)


@dataclass(init=False)
class OfFile(
    UserDict[str, Mapping[str, Any] | str | float | int | Dimensions | Collection[str]]
):
    """OfDict."""

    def __str__(self) -> str:
        string = ""

        for key, value in self.data.items():
            if isinstance(value, Mapping):
                string += f"{key}\n"
                string += "{\n"
                string += indent(str(OfFile(value)), "    ")
                string += "}\n"
            elif isinstance(value, (OfList, UniformList, NonUniformList)):
                string += f"{key} {value}\n"
            else:
                string += f"{key} {value};\n"

        return string

    def write(self, path: Path, overwrite: bool = False) -> None:
        logger.info("Going to write OF file %s", path)
        if path.exists() and not overwrite:
            raise FileExistsError(path)

        if not path.parent.exists():
            path.parent.mkdir(parents=True)

        text = str(OfFile(self.data))
        path.write_text(text)
