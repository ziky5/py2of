from dataclasses import dataclass
from typing import List
from enum import Enum
from typing import Sequence

from attr import field

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
        assert isinstance(self.elements, Sequence)
        python_element_type = type(
            self.elements[0]
        )  # TODO: make sure all the elements are the same type (__post_init___?)
        if python_element_type == int or python_element_type == float:
            self.element_type = ElementType.SCALAR
        elif python_element_type == OfVector:
            self.element_type = ElementType.VECTOR
        elif python_element_type == OfTensor:
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


def create_oflist_from_list(
    lst: List,
    name: str | None = None,
) -> OfList:
    assert isinstance(lst, List), "Input object must of type List."
    assert len(lst) in [
        1,
        3,
        9,
    ], f"Input list must have 1 element (scalar list), 3 elements (vector list) or 9 elements (tensor list). The input list has {len(lst)} elements."

    for i, sublst in enumerate(lst):
        assert isinstance(sublst, List), "All sublists must of type List."
        assert all(
            isinstance(x, (int, float)) for x in sublst
        ), 'All sublist must only contain "int" or "float".'
        assert len(lst[0]) == len(
            sublst
        ), f"All sublists must have the same length ({len(lst[0])}). Sublist on position {i} has length {len(sublst)}."

    assert (
        isinstance(name, str) or name is None
    ), 'argument "name" must be of type "str" or "None"'

    if not name:
        if len(lst[0]) == 1:
            name = "uniform"
        else:
            name = "nonuniform"

    oflist_elements = []

    if len(lst) == 1:
        oflist_elements = lst[0]
    elif len(lst) == 3:
        for i in range(len(lst[0])):
            vector = OfVector(
                x=lst[0][i],
                y=lst[1][i],
                z=lst[2][i],
            )
            oflist_elements.append(vector)
    elif len(lst) == 9:
        for i in range(len(lst[0])):
            tensor = OfTensor(
                xx=lst[0][i],
                xy=lst[1][i],
                xz=lst[2][i],
                yx=lst[3][i],
                yy=lst[4][i],
                yz=lst[5][i],
                zx=lst[6][i],
                zy=lst[7][i],
                zz=lst[8][i],
            )
            oflist_elements.append(tensor)

    return OfList(name=name, elements=oflist_elements)
