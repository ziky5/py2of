from collections import UserDict

from py2of.domain.dimensions import Dimensions
from py2of.domain.of_dict import OfFile


dct = {"FoamFile": OfFile({"version": 2.0})}

string = """\
FoamFile
{
    version 2.0;
}
"""


def test_can_be_created() -> None:
    OfFile()


def test_data_can_be_accessed() -> None:
    a = OfFile(dct)
    a.data


def test_str_can_be_used() -> None:
    str(OfFile(dct))


def test_str_nested_dict() -> None:
    output = str(OfFile(dct))
    assert output == string


def test_str_nested_ofdict() -> None:
    output = str(OfFile({"FoamFile": OfFile({"version": 2.0})}))
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
        OfFile({"solvers": OfFile({"p": OfFile({"solver": "PCG", "blah": 1000})})})
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
    output = str(OfFile({"dimensions": Dimensions()}))
    string = """\
dimensions [0 0 0 0 0 0 0];
"""
    assert output == string


def test_user_dict() -> None:
    output = str(OfFile({"FoamFile": UserDict({"class": "dictionary"})}))
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
    output = str(OfFile(python_dct))

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
