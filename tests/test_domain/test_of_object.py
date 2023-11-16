import pytest

from py2of.domain.of_object import OfObject
from py2of.domain.of_header import FieldClass

def test_create_of_object() -> None:
    ofobject = OfObject(
        objectName = 'genericObjectName',
        internalData= {
            'zone': [1,2,3,4,5]
        }
    )

def test_print_of_object() -> None:
    ofobject = OfObject(
        objectName = 'genericObjectName',
        internalData= {
            'zone': [1,2,3,4,5]
        }
    )

    expected = """\
FoamFile
{
    version 2.0;
    format ascii;
    class regIOobject;
    object genericObjectName;
}

1
(
zone
{
    type cellZone;
    cellLabels List<label>
    5
    (
    1
    2
    3
    4
    5
    );
}
)"""
    assert str(ofobject) == expected

def test_print_of_object_length2() -> None:
    ofobject = OfObject(
        objectName = 'genericObjectName',
        internalData= {
            'zone1': [1,2,3,4,5],
            'zone2': [6,7,8,9],
        }
    )

    expected = """\
FoamFile
{
    version 2.0;
    format ascii;
    class regIOobject;
    object genericObjectName;
}

2
(
zone1
{
    type cellZone;
    cellLabels List<label>
    5
    (
    1
    2
    3
    4
    5
    );
}
zone2
{
    type cellZone;
    cellLabels List<label>
    4
    (
    6
    7
    8
    9
    );
}
)"""
    assert str(ofobject) == expected

def test_print_of_object_different_class() -> None:
    ofobject = OfObject(
        objectName = 'genericObjectName',
        internalData = {
            'zone': [1,2,3,4,5]
        },
        className = FieldClass.ScalarField
    )

    expected = """\
FoamFile
{
    version 2.0;
    format ascii;
    class volScalarField;
    object genericObjectName;
}

1
(
zone
{
    type cellZone;
    cellLabels List<label>
    5
    (
    1
    2
    3
    4
    5
    );
}
)"""
    assert str(ofobject) == expected


def test_assert_object_name() -> None:
    with pytest.raises(AssertionError):
        ofobject = OfObject(
            objectName = 1,
            internalData = {
                'zone': [1,2,3,4,5]
            }
        )

def test_assert_data_dict() -> None:
    with pytest.raises(AssertionError):
        ofobject = OfObject(
            objectName = 1,
            internalData = [1,2,3,4,5]
        )

def test_assert_data_key_str() -> None:
    with pytest.raises(AssertionError):
        ofobject = OfObject(
            objectName = 'genericObjectName',
            internalData = {
                1: [1,2,3,4,5]
            }
        )

def test_assert_data_item_sequence() -> None:
    with pytest.raises(AssertionError):
        ofobject = OfObject(
            objectName = 'genericObjectName',
            internalData = {
                'zone': 1
            }
        )

def test_assert_class_name() -> None:
    with pytest.raises(AssertionError):
        ofobject = OfObject(
            objectName = 'genericObjectName',
            internalData = {
                'zone': [1,2,3,4,5],
            },
            className='regIOobject'
        )

# TODO test write function