from dataclasses import dataclass


@dataclass()
class OfVector:
    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"({self.x} {self.y} {self.z})"

    @classmethod
    def from_sequence(cls, seq):
        assert len(seq) == 3
        return cls(x=seq[0], y=seq[1], z=seq[2])
