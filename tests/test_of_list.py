import pytest

from ultimate_pyfoam.domain.of_list import OfList
from ultimate_pyfoam.domain.of_tensor import OfTensor
from ultimate_pyfoam.domain.of_vector import OfVector


def test_create() -> None:
    OfList("listName", [1, 2, 3])


def test_print_int() -> None:
    array = OfList("listName", [5, 12, 4])
    expected = """\
listName\tList<scalar>
3
(
5
12
4
);\
"""
    print(str(array))
    assert str(array) == expected


def test_print_vector() -> None:
    array = OfList(
        "listName", [OfVector(x=1.1, y=5.0, z=0.0), OfVector(x=1.0, y=4.0, z=2.5)]
    )
    expected = """\
listName\tList<vector>
2
(
(1.1 5.0 0.0)
(1.0 4.0 2.5)
);\
"""
    assert str(array) == expected


def test_print_tensor() -> None:
    array = OfList(
        "listName",
        [
            OfTensor(xx=1.1, xy=5.0, xz=0.0, yx=2, yy=3, yz=15, zx=0, zy=150, zz=3.876),
            OfTensor(xx=0, xy=0, xz=0, yx=0, yy=0, yz=0, zx=0, zy=0, zz=0),
        ],
    )
    expected = """\
listName\tList<tensor>
2
(
(
    1.1 5.0 0.0
    2 3 15
    0 150 3.876
)
(
    0 0 0
    0 0 0
    0 0 0
)
);\
"""
    assert str(array) == expected


def test_print_str() -> None:
    with pytest.raises(TypeError):
        array = OfList("listName", ["aaa"])  # type: ignore
        str(array)
