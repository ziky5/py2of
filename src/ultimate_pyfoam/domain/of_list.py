from dataclasses import dataclass
from typing import List


@dataclass()
class OfList:
    name: str
    num_of_elements: int
    element_type: List[int]
    elements: List[int]

    def __str__(self) -> str:
        string = f"{self.name}"
        string += "\t("
        string += " ".join([str(i) for i in self.elements])
        string += "\n);"
        return string
