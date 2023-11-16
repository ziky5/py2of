from dataclasses import dataclass
from enum import Enum
from typing import Any

from py2of.domain.of_file import OfFile


class FieldType(Enum):
    Dictionary = "dictionary"
    ScalarField = "volScalarField"
    VectorField = "volVectorField"
    TensorField = "volTensorField"
    RegIOObject = "regIOobject"


class DataFormat(Enum):
    Ascii = "ascii"
    Binary = "binary"


@dataclass()
class OfHeader:
    classname: FieldType
    name: str
    version: float = 2.0
    format: DataFormat = DataFormat.Ascii

    def __call__(self) -> dict:
        return {
            "version": self.version,
            "format": self.format.value,
            "class": self.classname.value,
            "object": self.name,
        }

    def __post_init__(self) -> None:
        assert isinstance(self.classname, FieldType)
        assert isinstance(self.format, DataFormat)
        assert isinstance(self.version, float)
        assert isinstance(self.name, str)
