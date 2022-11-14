from collections import UserDict
from collections.abc import Mapping
from dataclasses import dataclass
from textwrap import indent
from typing import Any
from typing import Collection

from ultimate_pyfoam.domain.dimensions import Dimensions


@dataclass(init=False)
class OfDict(
    UserDict[str, Mapping[str, Any] | str | float | int | Dimensions | Collection[str]]
):
    """OfDict."""

    def __str__(self) -> str:
        string = ""

        for key, value in self.data.items():
            if isinstance(value, OfDict):
                string += f"{key}\n"
                string += "{\n"
                string += indent(str(value), "    ")
                string += "}\n"
            else:
                string += f"{key} {value};\n"

        return string
