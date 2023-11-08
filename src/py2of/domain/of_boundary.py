from dataclasses import dataclass
from typing import Any


@dataclass
class OfBoundary:
    label: str

    def __hash__(self) -> int:
        return hash(self.label)

    def __call__(self) -> Any:
        return self.label
