from dataclasses import dataclass
import re

@dataclass()
class OF_units():
    SIunit: str #kgm-1s-2
    values = []

    def unit(self):
        units = ['kg','m','s','K','mol','A','cd']
        for u in units:
            if u in self.SIunit:
                z = re.search("("+f"[{u}]"+"{"+f"{len(u)}"+"})([0-9\\-]{1,5})", self.SIunit)
                #print(z)
                self.values.append(z[2])
            else: self.values.append(0)
        return self.values

    def __str__(self):
        string = f'[ {self.unit()[0]} {self.unit()[1]} {self.unit()[2]} {self.unit()[3]} {self.unit()[4]} {self.unit()[5]} {self.unit()[6]}]'
        return string