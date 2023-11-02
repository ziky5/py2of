from dataclasses import dataclass
from pathlib import Path
from collections.abc import Mapping, Sequence

from py2of.domain.of_list import ElementType, OfList
from py2of.domain.of_dict import OfDict
from py2of.domain.of_header import OfHeader, FieldClass

@dataclass()
class OfObject(): # TODO tests
    objectName: str
    internalData: Mapping[str, Sequence]
    className: FieldClass = FieldClass.RegIOObject

    def __post_init__(self) -> None:
        assert isinstance(self.objectName, str)
        assert isinstance(self.internalData, Mapping)
        for key, item in self.internalData.items():
            assert isinstance(key, str)
            assert isinstance(item, Sequence)
        assert isinstance(self.className, FieldClass)

        self.header = OfDict({
            'FoamFile': OfHeader(
                name = self.objectName,
                classname = self.className,
            ),
        })

        amended_data_dct = {}
        for key, item in self.internalData.items():
            amended_data_dct[key] = OfDict({
                "type": 'cellZone',
                "": OfList(
                    name='cellLabels',
                    elements=item,
                    element_type=ElementType.Label
                )
            })
        self.amended_data = OfDict(amended_data_dct)

    
    def write(self,location,mode='x'):
        path = Path(location) / self.objectName
        with open(path, mode) as f:
            f.write(f'{self.header}\n')
            f.write(f'{str(len(self.amended_data))}\n')
            f.write('(\n')
            f.write(f'{self.amended_data}')
            f.write(')')