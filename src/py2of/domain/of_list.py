from dataclasses import dataclass
from typing import List
from enum import Enum
from typing import Sequence
from numpy import ndarray

from attr import field
import numpy

from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


class ElementType(Enum):
    SCALAR = "scalar"
    VECTOR = "vector"
    TENSOR = "tensor"


@dataclass()
class OfList:
    name: str
    elements: List[int | float | OfVector | OfTensor]
    element_type: ElementType = field(init=False)

    def __post_init__(self):
        assert isinstance(self.elements, (Sequence, ndarray))

        is_scalar = False
        try:
            float(self.elements[0])
            is_scalar = True
        except:
            pass

        if is_scalar:
            self.element_type = ElementType.SCALAR
        elif isinstance(self.elements[0], OfVector):
            self.element_type = ElementType.VECTOR
        elif isinstance(self.elements[0], OfTensor):
            self.element_type = ElementType.TENSOR
        else:
            raise TypeError(f"Unknown type of list: {self.elements}")

    def __str__(self) -> str:
        string = f"{self.name}"
        string += f"\tList<{self.element_type.value}>\n{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.elements)

    @classmethod
    def from_components(
        cls,
        lst: Sequence,
        name: str | None = None,
    ) -> "OfList":
        lst = numpy.array(lst).T
        assert lst.ndim == 1 or lst.shape[1] in [
            3,
            9,
        ], f"Input sequence must have 1 element (scalar list), 3 elements (vector list) or 9 elements (tensor list). The input list has {lst.shape[1]} elements."

        if lst.ndim == 1:
            elements = lst.T
        elif lst.shape[1] == 3:
            elements = [OfVector.from_sequence(lst[i, :]) for i in range(lst.shape[0])]
        else:
            elements = [OfTensor.from_sequence(lst[i, :]) for i in range(lst.shape[0])]

        if name is None:
            name = "nonuniform"
            if len(elements) == 1:
                name = "uniform"

        return OfList(name=name, elements=elements)
