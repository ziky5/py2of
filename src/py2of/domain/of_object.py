from dataclasses import dataclass
from pathlib import Path
from collections.abc import Mapping, Sequence
from py2of.domain.of_file import OfFile

from py2of.domain.of_list import ElementType, OfList
from py2of.domain.of_header import OfHeader, FieldType


@dataclass()
class OfObject:  # TODO tests
    objectName: str
    internalData: Mapping[str, Sequence]
    className: FieldType = FieldType.RegIOObject

    def __post_init__(self) -> None:
        assert isinstance(self.objectName, str)
        assert isinstance(self.internalData, Mapping)
        for key, item in self.internalData.items():
            assert isinstance(key, str)
            assert isinstance(item, Sequence)
        assert isinstance(self.className, FieldType)

        self.header = OfFile(
            [{
                "FoamFile": OfHeader(
                    name=self.objectName,
                    classname=self.className,
                ),
            }]
        )

        amended_data_dct = {}
        for key, item in self.internalData.items():
            amended_data_dct[key] ={
                "type": "cellZone",
                "cellLabels": OfList(
                    name=None, elements=item, element_type=ElementType.Label
                ),
            }
        self.amended_data = OfFile([amended_data_dct])

    def __str__(self) -> str:
        string = ""
        string += f"{self.header}\n"
        string += f"{len(self.amended_data)}\n"
        string += "(\n"
        string += f"{self.amended_data}"
        string += ")"

        return string

    def write(self, location, mode="x"):
        path = Path(location) / self.objectName
        with open(path, mode) as f:
            f.write(str(self))
