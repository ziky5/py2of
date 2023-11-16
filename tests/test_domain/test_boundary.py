from py2of.domain.of_boundary import OfBoundary
from py2of.domain.of_file import OfFile


def test_boundary_call():
    boundary = OfBoundary(label="wall")
    assert boundary() == "wall"


def test_boundary_as_key():
    boundary = OfBoundary(label="wall")
    d = {boundary: "bc"}


def test_boundary_usage_with_offile():
    boundary = OfBoundary(label="wall")
    offile = OfFile([{"boundaryField": {boundary: "uniform 0"}}])
    should_be = """\
boundaryField
{
    wall uniform 0;
}
"""
    assert str(offile) == should_be
