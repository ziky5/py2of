from dataclasses import dataclass


@dataclass()
class OfTensor:
    xx: float
    xy: float
    xz: float
    yx: float
    yy: float
    yz: float
    zx: float
    zy: float
    zz: float

    def __str__(self) -> str:
        return f"""\
(
    {self.xx} {self.xy} {self.xz}
    {self.yx} {self.yy} {self.yz}
    {self.zx} {self.zy} {self.zz}
)\
"""

    @classmethod
    def from_sequence(cls, seq):
        assert len(seq) == 9
        return cls(
            xx=seq[0],
            xy=seq[1],
            xz=seq[2],
            yx=seq[3],
            yy=seq[4],
            yz=seq[5],
            zx=seq[6],
            zy=seq[7],
            zz=seq[8],
        )
