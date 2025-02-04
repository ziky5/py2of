from dataclasses import dataclass
from typing import Any
from enum import Enum


# Enums can't inherit from YamlSerializable and can't have yaml_tag attribute
class OfBoundaryType(Enum):
    PATCH = "patch"
    WALL = "wall"
    EMPTY = "empty"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar("!OfBoundaryType", node.value)

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls(node.value)

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


@dataclass(kw_only=True)
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
