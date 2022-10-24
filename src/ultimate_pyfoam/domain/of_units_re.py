import re
from dataclasses import dataclass
from typing import List


@dataclass()
class OfUnitsRe:
    SIunit: str

    def unit(self) -> List[str]:
        values = []
        units = ["kg", "m", "s", "K", "mol", "A", "cd"]
        for u in units:
            z = re.search(
                f"[{u}]" + "{" + f"{len(u)}" + "}([0-9\\-]{1,5})", self.SIunit
            )
            if z is None:
                values.append("0")
            else:
                values.append(z[1])
        print(values)
        return values

    def __str__(self) -> str:
        string = "[" + " ".join(self.unit()) + "]"
        return string
