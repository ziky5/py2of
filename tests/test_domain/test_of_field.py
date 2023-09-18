import pytest

from py2of.domain.of_field import OfField
from py2of.domain.of_header import OfHeader

def test_create_field() -> None:
    field = OfField()