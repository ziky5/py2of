from dataclasses import dataclass
from typing import Any, List

@dataclass()
class OfList():
    name: str
    num_of_elements: int
    element_type: List[int]
    elements: List[int]
    
    def __str__(self):
        string = f"{self.name}"
        string += "\t("
        string += ' '.join(self.elements)
            
        string += "\n);"