from dataclasses import dataclass
from typing import Mapping


@dataclass()
class OfDict():
    name: str
    content: Mapping

    def __str__(self):
        string = f"{self.name}"
        string += "\n{"

        for key, value in self.content.items():
            string += f"\n    {key} {value};"

        string += "\n}"
        return string