from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum
from typing import Sequence
from numpy import ndarray

from attr import field
import numpy

from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector

class ElementType(Enum):
    Scalar = "scalar"
    Vector = "vector"
    Tensor = "tensor"
    Label = "label"

@dataclass()
class OfList:
    name: str | None                                                # TODO - name not mandatory
    elements: Sequence[int | float | OfVector | OfTensor]           # TODO - OfList can be sequence of anything
    element_type: ElementType | None = None
    write_header: bool = True

    def __post_init__(self):
        assert isinstance(self.name, str | None),  "'name' has to be of type 'str' or 'None'"
        assert isinstance(self.elements, Sequence), "'elements' has to be a Sequence"
        assert all(isinstance(x, int | float | OfVector | OfTensor) for x in self.elements), "'elements' has to be Sequence of 'int', 'float', 'OfVector' or 'OfTensor'"
        assert all(isinstance(x, type(self.elements[0])) for x in self.elements), "All elements of parameter 'elements' has to be of the same type"
        assert isinstance(self.element_type, ElementType | None), "'element_type' has to of type 'ElementType'"
        assert isinstance(self.write_header, bool), "'write_header' has to be of type 'bool'"

        if not self.element_type:
            if isinstance(self.elements[0], int | float):
                self.element_type = ElementType.Scalar
            elif isinstance(self.elements[0], OfVector):
                self.element_type = ElementType.Vector
            elif isinstance(self.elements[0], OfTensor):
                self.element_type = ElementType.Tensor

    def __str__(self) -> str:
        string = ""
        if self.write_header:
            if self.name:
                string += f"{self.name}\t"
            string += "List"
            if self.element_type:
                string += f"<{self.element_type.value}>\n"
        string += f"{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.values)

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
            elements = [OfVector(lst[i, :]) for i in range(lst.shape[0])]
        else:
            elements = [OfTensor.from_sequence(lst[i, :]) for i in range(lst.shape[0])]

        if name is None:
            name = "nonuniform"
            if len(elements) == 1:
                name = "uniform"

        return OfList(name=name, values=elements)


@dataclass
class UniformList:
    value: int | float | OfVector | OfTensor

    def __str__(self) -> str:
        return f"uniform {self.value}"


@dataclass
class NonUniformList:
    values: Iterable[int | float | OfVector | OfTensor]

    def __str__(self) -> str:
        return str(OfList("nonuniform", self.values))
