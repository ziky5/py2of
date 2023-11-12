from dataclasses import dataclass
from typing import Any
from enum import StrEnum, auto


class OfBoundaryType(StrEnum):
    PATCH = "patch"
    WALL = "wall"
    EMPTY = "empty"


@dataclass
class OfBoundary:
    label: str
    type: OfBoundaryType = OfBoundaryType.PATCH

    def __post_init__(self):
        self.label = str(self.label)

    def __hash__(self) -> int:
        return hash(self.label)

    def __call__(self) -> Any:
        return self.label

    def __repr__(self):
        return self.label
