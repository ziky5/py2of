
import pytest
from ultimate_pyfoam.domain.vector import OfVector

def test_vector_init():
    OfVector(1.0, 1.1, 1.2)
    OfVector(x = 1.0, y = 1.1, z = 1.2)

def test_vector_printable():
    vec = OfVector(1.0, 1.1, 1.2)
    str(vec)

def test_vector_prints_correctly():
    vec = OfVector(1.0, 1.1, 1.2)
    test_output = "(1.0 1.1 1.2)"
    assert test_output == str(vec)