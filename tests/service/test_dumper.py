from pathlib import Path

import pytest

from ultimate_pyfoam.domain.of_dict import OfDict
from ultimate_pyfoam.service.dumper import Dumper


def test_init(tmp_path: Path) -> None:
    Dumper(content=OfDict())


def test_can_write_file(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())
    d.write(path=tmp_path / "dumpedFile")
    assert (tmp_path / "dumpedFile").exists()


def test_writes_content_correctly(tmp_path: Path) -> None:
    string = "application scalarTransportFoam;"
    dct = OfDict({"application": "scalarTransportFoam"})

    d = Dumper(content=dct)
    d.write(path=tmp_path / "controlDict")

    written_string = Path(tmp_path / "controlDict").read_text().strip()
    assert string == written_string


def test_refuses_to_overwrite_by_default(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())
    d.write(path=tmp_path / "dumpedFile")

    with pytest.raises(FileExistsError):
        d.write(path=tmp_path / "dumpedFile")


def test_overwrite_when_specified(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())
    d.write(path=tmp_path / "dumpedFile")
    d.write(path=tmp_path / "dumpedFile", overwrite=True)


def test_create_directory_in_path_if_nonexistent(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())
    d.write(path=tmp_path / "constant/dumpedFile")

    assert (tmp_path / "constant" / "dumpedFile").exists()


def test_create_multiple_directories_in_path_if_nonexistent(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())
    d.write(path=tmp_path / "constant/one_more_directory/dumpedFile")

    assert (tmp_path / "constant" / "one_more_directory" / "dumpedFile").exists()


def test_cannot_write_to_directory(tmp_path: Path) -> None:
    d = Dumper(content=OfDict())

    with pytest.raises(IsADirectoryError):
        d.write(path=tmp_path)

def test_basic_python_dict(tmp_path: Path) -> None:
    string = "application scalarTransportFoam;"
    dct = {"application": "scalarTransportFoam"}

    d = Dumper(content=dct)
    d.write(path=tmp_path / "controlDict")

    written_string = Path(tmp_path / "controlDict").read_text().strip()
    assert string == written_string
