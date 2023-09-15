from collections import UserDict

from py2of.domain.dimensions import Dimensions
from py2of.domain.of_dict import OfDict


dct = {"FoamFile": OfDict({"version": 2.0})}

string = """\
FoamFile
{
    version 2.0;
}
"""


def test_can_be_created() -> None:
    OfDict()


def test_data_can_be_accessed() -> None:
    a = OfDict(dct)
    a.data


def test_str_can_be_used() -> None:
    str(OfDict(dct))


def test_str_nested_dict() -> None:
    output = str(OfDict(dct))
    assert output == string


def test_str_nested_ofdict() -> None:
    output = str(OfDict({"FoamFile": OfDict({"version": 2.0})}))
    assert output == string


# def test_multiple_data_entries():
#    output = str(OfDict(name="FoamFile", content={"version": [2.0, 3.0]}))
#    string = """\
# FoamFile
# {
#    version 2.0 3.0;
# }\
# """
#    assert output == string


def test_triple_nested_ofdict() -> None:
    output = str(
        OfDict({"solvers": OfDict({"p": OfDict({"solver": "PCG", "blah": 1000})})})
    )
    string = """\
solvers
{
    p
    {
        solver PCG;
        blah 1000;
    }
}
"""
    assert output == string


def test_dimensions_as_value() -> None:
    output = str(OfDict({"dimensions": Dimensions()}))
    string = """\
dimensions [0 0 0 0 0 0 0];
"""
    assert output == string


def test_user_dict() -> None:
    output = str(OfDict({"FoamFile": UserDict({"class": "dictionary"})}))
    string = """\
FoamFile
{
    class dictionary;
}
"""
    assert output == string


def test_python_dict() -> None:
    python_dct = {
        "FoamFile": {
            "format": "ascii",
            "class": "dictionary",
            "location": '"system"',
            "object": "controlDict",
        },
        "application": "scalarTransportFoam",
        "startFrom": "startTime",
    }
    output = str(OfDict(python_dct))

    string = """\
FoamFile
{
    format ascii;
    class dictionary;
    location "system";
    object controlDict;
}
application scalarTransportFoam;
startFrom startTime;
"""
    assert output == string
