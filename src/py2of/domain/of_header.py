from dataclasses import dataclass
from enum import Enum

# @dataclass()
# class OfHeader:
#     placeholder: str


class FieldType(Enum):
    dictionary = "dictionary"
    volScalarField = "volScalarField"
    volVectorField = "volVectorField"
    volTensorField = "volTensorField"


@dataclass()
class OfHeader:
    classname: FieldType
    location: str
    name: str
    version: float = 2.0
    format: str = 'ascii'

    def __post_init__(self):
        assert isinstance(self.classname, FieldType)

#header = OfHeader(classname=FieldType.)