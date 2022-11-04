import pytest

from ultimate_pyfoam.domain.of_list import OfList
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
    print(str(array))
    assert str(array) == expected


def test_print_str() -> None:
    with pytest.raises(TypeError):
        array = OfList("listName", ["aaa"])  # type: ignore
        str(array)
