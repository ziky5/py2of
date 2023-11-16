from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
import logging

from py2of.domain.of_list import OfList, NonUniformList, UniformList

logger = logging.getLogger(__name__)


@dataclass(init=False)
class OfFile(
    list
    # UserDict[str, Mapping[str, Any] | str | float | int | Dimensions | Collection[str]]
):
    """OfDict."""

    def __str__(self) -> str:
        string = ""

        for item in iter(self):
            if callable(item):
                item = item()

            if isinstance(item, Mapping):
                string += OfList.print_mapping(item)
            else:
                string += str(item)

        return string

    def write(self, path: Path, overwrite: bool = False) -> None:
        path = Path(path)
        logger.info("Going to write OF file %s", path)
        if path.exists() and not overwrite:
            raise FileExistsError(path)

        if not path.parent.exists():
            path.parent.mkdir(parents=True)

        text = str(OfFile(self))
        path.write_text(text)
