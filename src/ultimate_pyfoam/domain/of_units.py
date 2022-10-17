from dataclasses import dataclass
import re

@dataclass()
class OF_units():
    SIunit: str #kgm-1s-2

    def __str__(self):
        if 'm' in self.SIunit:
            m = re.search('[m]{1}([0-9\-]{1,5})', self.SIunit) 
        string = '[{kg}]'
        return string