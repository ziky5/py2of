from dataclasses import dataclass, field
from typing import Union

from py2of.domain.of_list import NonUniformList, OfList, UniformList
from py2of.domain.of_file import OfFile
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_header import OfHeader
from py2of.domain.of_header import FieldType
from py2of.domain.of_list import ElementType
from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


@dataclass()
class OfField(OfFile):
    fieldName: str
    dimensions: Dimensions
    internalData: UniformList | NonUniformList
    boundaryData: Union[OfList, OfFile]
    data: dict = field(init=False, repr=False)

    def __post_init__(self) -> None:
        assert isinstance(self.dimensions, Dimensions)
        assert isinstance(self.internalData, (UniformList, NonUniformList))

        if hasattr(self.internalData, "value"):
            probe = self.internalData.value
        else:
            probe = self.internalData.values[0]

        try:
            float(probe)
            field_type = FieldType.ScalarField
        except TypeError:
            if isinstance(probe, OfVector):
                field_type = FieldType.VectorField
            elif isinstance(probe, OfTensor):
                field_type = FieldType.TensorField
            else:
                raise TypeError(f"unknown type of internalData: {self.internalData}")

        header = OfHeader(
            name=self.fieldName,
            classname=field_type,
        )

        self.data = {
            "FoamFile": header,
            "dimensions": self.dimensions,
            "internalField": self.internalData,
            "boundaryField": self.boundaryData,
        }
