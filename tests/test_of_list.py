from ultimate_pyfoam.domain.of_list import OfList


def test_create():
    OfList("list", 5, [], [1, 2, 3])


def test_print():
    array = OfList("list", 5, [], [1, 2, 3])
    expected = """\
    list    List[int]
    5
    (
        [1,2,3]
    )\
    """
    assert str(array) == expected
