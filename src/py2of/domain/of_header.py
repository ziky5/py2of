from dataclasses import dataclass
from enum import Enum

# @dataclass()
# class OfHeader:
#     placeholder: str


class FieldType(Enum):
    Dictionary = "dictionary"
    ScalarField = "volScalarField"
    VectorField = "volVectorField"
    TensorField = "volTensorField"

class DataFormat(Enum):
    Ascii = "ascii"
    Binary = "binary"

@dataclass()
class OfHeader:
    classname: FieldType
    location: str
    name: str
    version: float = 2.0
    format: DataFormat = DataFormat.Ascii

    def __post_init__(self):
        assert isinstance(self.classname, FieldType)
        assert isinstance(self.format, DataFormat)
        assert isinstance(self.version, float)
        assert isinstance(self.name, str)
        assert isinstance(self.location, str)
        try:
            float(self.location)
        except:
            raise AssertionError('"location" must be convertible to a number.')
