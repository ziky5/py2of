from dataclasses import dataclass
from typing import Sequence
from enum import Enum

from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector

class ElementType(Enum):
    Scalar = "scalar"
    Vector = "vector"
    Tensor = "tensor"
    Label = "label"

@dataclass()
class OfList:
    name: str | None
    elements: Sequence[int | float | OfVector | OfTensor]
    element_type: ElementType | None = None
    write_header: bool = True

    def __post_init__(self):
        assert isinstance(self.elements, Sequence)
        assert isinstance(self.name, str | None) # TODO test types and stuff
        for iter_element in self.elements:
            assert isinstance(iter_element, int | float | OfVector | OfTensor)
        assert isinstance(self.element_type, ElementType | None)
        assert isinstance(self.write_header, bool)

        if not self.element_type:
            if isinstance(self.elements[0], int | float):  #TODO check if all elements are of the same type
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
            string += f"List<{self.element_type.value}>\n"
        string += f"{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.elements)

    @classmethod
    def from_components_lists(
            cls: "OfList",
            lst: Sequence[Sequence],
            name: str | None = None,
        ) -> "OfList":
        assert isinstance(lst, Sequence), 'Input object must of type List.'
        assert len(lst) in [1, 3, 9], f'Input list must have 1 element (scalar list), 3 elements (vector list) or 9 elements (tensor list). The input list has {len(lst)} elements.'

        for i, sublst in enumerate(lst):
            assert isinstance(sublst, Sequence), 'All sublists must of type List.'
            assert all(isinstance(x, (int, float)) for x in sublst), 'All sublist must only contain "int" or "float".'
            assert len(lst[0]) == len(sublst), f'All sublists must have the same length ({len(lst[0])}). Sublist on position {i} has length {len(sublst)}.'

        assert isinstance(name, str) or name is None, 'argument "name" must be of type "str" or "None"'

        if not name:
            if len(lst[0]) == 1:
                name = 'uniform'
            else:
                name = 'nonuniform'

        oflist_elements = []

        if len(lst) == 1:
            oflist_elements = lst[0]
        elif len(lst) == 3:
            for i in range(len(lst[0])):
                vector = OfVector(
                    x = lst[0][i],
                    y = lst[1][i],
                    z = lst[2][i],
                )
                oflist_elements.append(vector)
        elif len(lst) == 9:
            for i in range(len(lst[0])):
                tensor = OfTensor(
                    xx = lst[0][i],
                    xy = lst[1][i],
                    xz = lst[2][i],
                    yx = lst[3][i],
                    yy = lst[4][i],
                    yz = lst[5][i],
                    zx = lst[6][i],
                    zy = lst[7][i],
                    zz = lst[8][i],
                )
                oflist_elements.append(tensor)

        return cls(name = name, elements = oflist_elements)
