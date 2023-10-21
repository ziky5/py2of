from collections import UserDict
from pathlib import Path
import pytest

from py2of.domain.dimensions import Dimensions
from py2of.domain.of_file import OfFile


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


def test_can_write_file(tmp_path: Path) -> None:
    d = OfFile()
    d.write(path=tmp_path / "dumpedFile")
    assert (tmp_path / "dumpedFile").exists()


def test_writes_content_correctly(tmp_path: Path) -> None:
    string = "application scalarTransportFoam;"
    dct = OfFile({"application": "scalarTransportFoam"})

    d = OfFile(dct)
    d.write(path=tmp_path / "controlDict")

    written_string = Path(tmp_path / "controlDict").read_text().strip()
    assert string == written_string


def test_refuses_to_overwrite_by_default(tmp_path: Path) -> None:
    d = OfFile()
    d.write(path=tmp_path / "dumpedFile")

    with pytest.raises(FileExistsError):
        d.write(path=tmp_path / "dumpedFile")


def test_overwrite_when_specified(tmp_path: Path) -> None:
    d = OfFile()
    d.write(path=tmp_path / "dumpedFile")
    d.write(path=tmp_path / "dumpedFile", overwrite=True)


def test_create_directory_in_path_if_nonexistent(tmp_path: Path) -> None:
    d = OfFile()
    d.write(path=tmp_path / "constant/dumpedFile")

    assert (tmp_path / "constant" / "dumpedFile").exists()


def test_create_multiple_directories_in_path_if_nonexistent(tmp_path: Path) -> None:
    d = OfFile()
    d.write(path=tmp_path / "constant/one_more_directory/dumpedFile")

    assert (tmp_path / "constant" / "one_more_directory" / "dumpedFile").exists()


def test_cannot_write_to_directory(tmp_path: Path) -> None:
    d = OfFile()

    with pytest.raises(IsADirectoryError):
        d.write(path=tmp_path, overwrite=True)


def test_content_is_basic_python_dict(tmp_path: Path) -> None:
    string = "application scalarTransportFoam;"
    dct = {"application": "scalarTransportFoam"}

    d = OfFile(dct)
    d.write(path=tmp_path / "controlDict")

    written_string = Path(tmp_path / "controlDict").read_text().strip()
    assert string == written_string
