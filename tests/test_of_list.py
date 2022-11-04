from ultimate_pyfoam.domain.of_list import OfList


def test_create() -> None:
    OfList("listName", [], [1, 2, 3])


def test_print() -> None:
    array = OfList("listName", [], [5, 12, 4])
    expected = """\
listName\tList[int]
3
(
5
12
4
);\
"""
    print(str(array))
    assert str(array) == expected
