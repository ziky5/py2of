from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass
class OfVector:
    values: Sequence[int | float]

    def __post_init__(self):
        assert len(self.values) == 3

    def __str__(self) -> str:
        return f"({self.values[0]} {self.values[1]} {self.values[2]})"
