from dataclasses import dataclass
from typing import List


@dataclass()
class OfList:
    name: str
    element_type: List[int]
    elements: List[int]

    def __str__(self) -> str:
        string = f"{self.name}"
        string += f"\tList[int]\n{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.elements)
