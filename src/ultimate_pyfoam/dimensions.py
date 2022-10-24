from dataclasses import dataclass
from typing import List


@dataclass()
class OfDimensions:
    content: List[int]

    def __str__(self) -> str:
        if len(self.content) != 7:
            raise Exception()

        output = "["
        for i in range(len(self.content) - 1):
            output += f"{self.content[i]} "
        output += f"{self.content[len(self.content) - 1]}"
        output += "]"
        return output
