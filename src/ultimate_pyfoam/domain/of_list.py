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
        string += "\tList[int]\n" + str(self.num_of_elements) + "\n(\n"
        string += "\t[" + ",".join([str(i) for i in self.elements]) + "]"
        string += "\n);"
        return string
