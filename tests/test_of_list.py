from ultimate_pyfoam.domain.of_list import OfList


def test_create() -> None:
    OfList("list", 5, [], [1, 2, 3])


def test_print() -> None:
    array = OfList("list", 5, [], [1, 2, 3])
    expected = """list\tList[int]
5
(
\t[1,2,3]
);\
"""
    print(str(array))
    assert str(array) == expected
