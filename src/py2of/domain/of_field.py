from dataclasses import dataclass
from typing import Union

from py2of.domain.of_list import OfList
from py2of.domain.of_dict import OfDict
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_header import OfHeader
from py2of.domain.of_header import FieldClass

@dataclass()
class OfField(OfDict):
    fieldName: str
    dimension: Dimensions
    internalData: Union[OfList, OfDict]
    boundaryData: Union[OfList, OfDict]

    def __post_init__(self) -> None:
        assert isinstance(self.fieldName, str)
        assert isinstance(self.dimension, Dimensions)
        assert isinstance(self.internalData, (OfList, OfDict))
        assert isinstance(self.boundaryData, (OfList, OfDict))

        if isinstance(self.internalData, OfList):
            if self.internalData.element_type == 'scalar':
                self.fieldclass = FieldClass.ScalarField
            elif self.internalData.element_type == 'vector':
                self.fieldclass = FieldClass.VectorField
            elif self.internalData.element_type == 'tensor':
                self.fieldclass = FieldClass.TensorField
        elif isinstance(self.internalData, OfDict):
            self.fieldclass = FieldClass.Dictionary

        header = OfHeader(
            name = self.fieldName,
            classname = self.fieldclass,
        )

        self.data = {
            'FoamFile': header,
            'dimensions': self.dimension,
            'internalField': self.internalData,
            'boundaryField': self.boundaryData,
        }