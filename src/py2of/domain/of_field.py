from dataclasses import dataclass, field
from typing import Union

from py2of.domain.of_list import OfList
from py2of.domain.of_file import OfFile
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_header import OfHeader
from py2of.domain.of_header import FieldClass
from py2of.domain.of_list import ElementType

ELEMENT_TO_FIELD_TYPE = {
    ElementType.SCALAR: FieldClass.ScalarField,
    ElementType.VECTOR: FieldClass.VectorField,
    ElementType.TENSOR: FieldClass.TensorField,
}


@dataclass()
class OfField(OfFile):
    fieldName: str
    dimension: Dimensions
    internalData: Union[OfList, OfFile]
    boundaryData: Union[OfList, OfFile]
    data: dict = field(init=False, repr=False)

    def __post_init__(self) -> None:
        assert isinstance(self.fieldName, str)
        assert isinstance(self.dimension, Dimensions)
        assert isinstance(self.internalData, (OfList, OfFile))
        assert isinstance(self.boundaryData, (OfList, OfFile))

        if isinstance(self.internalData, OfList):
            self.fieldclass = ELEMENT_TO_FIELD_TYPE[self.internalData.element_type]
        elif isinstance(self.internalData, OfFile):
            self.fieldclass = FieldClass.Dictionary

        header = OfHeader(
            name=self.fieldName,
            classname=self.fieldclass,
        )

        self.data = {
            "FoamFile": header,
            "dimensions": self.dimension,
            "internalField": self.internalData,
            "boundaryField": self.boundaryData,
        }
