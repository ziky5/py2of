from dataclasses import dataclass
from typing import Sequence

from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


@dataclass()
class OfList:
    name: str
    elements: Sequence[int | float | OfVector | OfTensor]

    def __str__(self) -> str:
        string = f"{self.name}"
        string += f"\tList<{self.element_type}>\n{len(self)}\n(\n"
        for i in self.elements:
            string += f"{i}\n"
        string += ");"
        return string

    def __len__(self) -> int:
        return len(self.elements)

    @property
    def element_type(self) -> str:
        python_element_type = type(
            self.elements[0]
        )  # TODO: make sure all the elements are the same type (__post_init___?)
        if python_element_type == int or python_element_type == float:
            return "scalar"
        elif python_element_type == OfVector:
            return "vector"
        elif python_element_type == OfTensor:
            return "tensor"
        else:
            raise TypeError()

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
