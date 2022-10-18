from dataclasses import dataclass
import re

@dataclass()
class OF_units():
    SIunit: str #kgm-1s-2
    values = []

    def unit(self):
        units = ['kg','m','s','K','mol','A','cd']
        for u in units:
            z = re.search("(" + f"[{u}]" + "{" + f"{len(u)}" + "})([0-9\\-]{1,5})", self.SIunit)
            if z is None:
                self.values.append('0')
            else: self.values.append(z[2])
        return self.values

    def __str__(self):
        string = "[" + " ".join(self.unit()) + "]"
        return string