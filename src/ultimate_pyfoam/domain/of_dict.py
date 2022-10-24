from collections import UserDict
from dataclasses import dataclass
from textwrap import indent
from typing import Any


@dataclass(init=False)
class OfDict(UserDict[Any, Any]):
    pass

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
