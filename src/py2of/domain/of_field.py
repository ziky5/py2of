from dataclasses import dataclass, field
from typing import Mapping, Union
from py2of.domain.of_boundary import OfBoundary
from py2of.domain.of_boundary_conditions import OfBoundaryCondition

from py2of.domain.of_list import NonUniformList, OfList, UniformList
from py2of.domain.of_file import OfFile
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_header import OfHeader
from py2of.domain.of_header import FieldType
from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_vector import OfVector


@dataclass()
class OfField(OfFile):
    fieldName: str
    dimensions: Dimensions
    internalData: UniformList | NonUniformList
    boundaryData: Mapping[OfBoundary, OfBoundaryCondition]
    header: Mapping = field(init=False, repr=False)

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

        self.header = OfHeader(
            name=self.fieldName,
            classname=field_type,
        )

        self.append(
            {
                "FoamFile": self.header,
                "dimensions": self.dimensions,
                "internalField": self.internalData,
                "boundaryField": self.boundaryData,
            }
        )
