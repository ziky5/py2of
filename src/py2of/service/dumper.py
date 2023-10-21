from dataclasses import dataclass
from pathlib import Path
from typing import Any
from typing import Mapping

from py2of.domain.of_file import OfFile


@dataclass()
class Dumper:
    content: Mapping[str, Any]

    def write(self, path: Path, overwrite: bool = False) -> None:
        if path.exists() and not overwrite:
            raise FileExistsError(path)

        if not path.parent.exists():
            path.parent.mkdir(parents=True)

        text = str(OfFile(self.content))
        path.write_text(text)
