import pytest

from py2of.domain.of_header import OfHeader

def test_create() -> None:
    header = OfHeader(classname='volVectorField', location='"0.000e+00"', name='genericObject')

def test_print() -> None:
    header = OfHeader(classname='volVectorField', location='"0.000e+00"', name='genericObject')
    expected_output = """\
{
    version 2.0;
    format ascii;
    class volVectorField;
    location "0.000e+00";
    object genericObject;
}
"""
    assert str(header) == expected_output

def test_class_type() -> None:
    with pytest.raises(TypeError):
        header = OfHeader(classname='vectorField', location='"0.000e+00"', name='genericObject')
        str(header)