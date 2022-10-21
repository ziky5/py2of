from collections import UserDict
from dataclasses import dataclass


@dataclass(init=False)
class OfDict(UserDict):
    pass


#    def __str__(self):
#        string = f"{self.name}"
#        string += "\n{"
#
#        for key, value in self.content.items():
#            string += f"\n    {key} {value};"
#
#        string += "\n}"
#        return string
