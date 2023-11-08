from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any
from py2of.domain.of_list import NonUniformList, UniformList
from py2of.domain.of_tensor import OfTensor

from py2of.domain.of_vector import OfVector


@dataclass
class OfBoundaryCondition(ABC):
    pass

    @abstractmethod
    def __call__(self) -> Any:
        pass


@dataclass
class FixedValue(OfBoundaryCondition):
    value: UniformList | NonUniformList

    def __call__(self) -> dict:
        return {"type": "fixedValue", "value": str(self.value)}
