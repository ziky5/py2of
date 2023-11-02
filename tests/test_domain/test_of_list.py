import pytest

from py2of.domain.of_list import OfList
from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


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
    with pytest.raises(AssertionError):
        array = OfList("listName", ["aaa"])  # type: ignore
        str(array)




def test_nonuniform_scalar_oflist_from_list() -> None:
    oflist = OfList.from_components_lists([[1, 2.3, 8]])
    expected_output = '''\
nonuniform\tList<scalar>
3
(
1
2.3
8
);'''
    assert str(oflist) == expected_output

def test_nonuniform_vector_oflist_from_list() -> None:
    oflist = OfList.from_components_lists([[1, 2.3, 8, 3], [2, 3.8, 15, 9], [3, 5.2, 123, 27]])
    expected_output = '''\
nonuniform\tList<vector>
4
(
(1 2 3)
(2.3 3.8 5.2)
(8 15 123)
(3 9 27)
);'''
    assert str(oflist) == expected_output

def test_nonuniform_tensor_oflist_from_list() -> None:
    oflist = OfList.from_components_lists([[1, 2.3], [2, 3.8], [3, 5.2], [4, 7.0], [5, 16.4], [6, 7.8], [7, 15.2], [8, 0.0], [9, 3.3]])
    expected_output = '''\
nonuniform\tList<tensor>
2
(
(
    1 2 3
    4 5 6
    7 8 9
)
(
    2.3 3.8 5.2
    7.0 16.4 7.8
    15.2 0.0 3.3
)
);'''
    assert str(oflist) == expected_output

def test_uniform_scalar_oflist_from_list() -> None:
    oflist = OfList.from_components_lists([[1]])
    expected_output = '''\
uniform\tList<scalar>
1
(
1
);'''
    assert str(oflist) == expected_output

def test_named_scalar_oflist_from_list() -> None:
    oflist = OfList.from_components_lists([[1, 2.3, 8]], name='genericOfList')
    expected_output = '''\
genericOfList\tList<scalar>
3
(
1
2.3
8
);'''
    assert str(oflist) == expected_output

def test_type_of_name_named_oflist_from_list() -> None:
    with pytest.raises(AssertionError):
        oflist = OfList.from_components_lists([[1, 2.3, 8]], name=2)

def test_type_in_list_oflist_from_list() -> None:
    with pytest.raises(AssertionError):
        oflist = OfList.from_components_lists([['1', '2.3', '8']])

def test_sublists_present_oflist_from_list() -> None:
    with pytest.raises(AssertionError):
        oflist = OfList.from_components_lists([1, 2.3, 8])

def test_sublists_length_oflist_from_list() -> None:
    with pytest.raises(AssertionError):
        oflist = OfList.from_components_lists([[1, 2.3, 8],[1, 2.3, 8],[1, 8]])

def test_numer_of_sublists_length_oflist_from_list() -> None:
    with pytest.raises(AssertionError):
        oflist = OfList.from_components_lists([[1, 2.3, 8],[1, 2.3, 8],[1, 8, 4],[1, 8, 4]])