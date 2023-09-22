from dataclasses import dataclass
from enum import Enum

from py2of.domain.of_dict import OfDict

class FieldClass(Enum):
    Dictionary = "dictionary"
    ScalarField = "volScalarField"
    VectorField = "volVectorField"
    TensorField = "volTensorField"

class DataFormat(Enum):
    Ascii = "ascii"
    Binary = "binary"

@dataclass()
class OfHeader(OfDict):
    classname: FieldClass
    name: str
    version: float = 2.0
    format: DataFormat = DataFormat.Ascii

    def __post_init__(self) -> None:
        assert isinstance(self.classname, FieldClass)
        assert isinstance(self.format, DataFormat)
        assert isinstance(self.version, float)
        assert isinstance(self.name, str)

        self.data = {
            'version': self.version,
            'format': self.format.value,
            'class': self.classname.value,
            'object': self.name,
        }
