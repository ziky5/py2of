from dataclasses import dataclass, field
from pathlib import Path

from py2of.domain.of_list import OfList, ElementType
from py2of.domain.of_dict import OfDict
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_header import OfHeader
from py2of.domain.of_header import FieldClass

from py2of.service.dumper import Dumper

@dataclass()
class OfField(OfDict):
    fieldName: str
    dimension: Dimensions
    internalData: OfList
    boundaryData: OfDict
    fieldClass: FieldClass = field(init=False, repr=False)
    data: dict = field(init=False, repr=False)

    def __post_init__(self) -> None:
        assert isinstance(self.fieldName, str)
        assert isinstance(self.dimension, Dimensions)
        assert isinstance(self.internalData, OfList)
        assert isinstance(self.boundaryData, OfDict)

        if isinstance(self.internalData, OfList):
            if self.internalData.element_type == ElementType.Scalar:
                self.fieldClass = FieldClass.ScalarField
            elif self.internalData.element_type == ElementType.Vector:
                self.fieldClass = FieldClass.VectorField
            elif self.internalData.element_type == ElementType.Tensor:
                self.fieldClass = FieldClass.TensorField
        elif isinstance(self.internalData, OfDict):
            self.fieldClass = FieldClass.Dictionary

        header = OfHeader(
            name = self.fieldName,
            classname = self.fieldClass,
        )

        self.data = {
            'FoamFile': header,
            'dimensions': self.dimension,
            'internalField': self.internalData,
            'boundaryField': self.boundaryData,
        }
    
    def write(self,location):
        dumper = Dumper(self.data)
        path = Path(location) / self.fieldName
        dumper.write(path, overwrite=True)