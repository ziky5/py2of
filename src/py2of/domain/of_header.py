from dataclasses import dataclass
from enum import Enum

from py2of.domain.of_dict import OfDict

class FieldOrder(Enum):
    Dictionary = "dictionary"
    ScalarField = "volScalarField"
    VectorField = "volVectorField"
    TensorField = "volTensorField"

class DataFormat(Enum):
    Ascii = "ascii"
    Binary = "binary"

@dataclass()
class OfHeader:
    classname: FieldOrder
    name: str
    version: float = 2.0
    format: DataFormat = DataFormat.Ascii

    def __str__(self) -> str:
        header_dict = OfDict({
            'version': self.version,
            'format': self.format.value,
            'class': self.classname.value,
            'object': self.name,
        })
        return str(header_dict)

    def __post_init__(self):
        assert isinstance(self.classname, FieldOrder)
        assert isinstance(self.format, DataFormat)
        assert isinstance(self.version, float)
        assert isinstance(self.name, str)
