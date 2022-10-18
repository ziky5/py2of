from dataclasses import dataclass
import re

@dataclass()
class OF_units():
    SIunit: str

    def unit(self):
        values = []
        units = ['kg','m','s','K','mol','A','cd']
        for u in units:
            z = re.search(f"[{u}]" + "{" + f"{len(u)}" + "}([0-9\\-]{1,5})", self.SIunit)
            if z is None:
                values.append('0')
            else: values.append(z[1])
        print(values)
        return values

    def __str__(self):
        string = "[" + " ".join(self.unit()) + "]"
        return string