from collections import UserDict
from dataclasses import dataclass
from textwrap import indent
from typing import Union


@dataclass(init=False)
class OfDict(UserDict[str, Union[str, float, int, bool, "OfDict"]]):
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
