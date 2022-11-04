from ultimate_pyfoam.dimensions import OfDimensions
import pytest



def test_dimenions():
    output = str(OfDimensions([0, 2, -1, 0, 0, 0, 0]))
    s = "[0 2 -1 0 0 0 0]"
    assert output == s

def test_dimensions_size():
    with pytest.raises(Exception):
        d = OfDimensions([0, 2, -1, 0, 0, 0])
        str(d)