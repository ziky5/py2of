import pytest

from py2of.domain.of_header import OfHeader, FieldClass, DataFormat

def test_create_header() -> None:
    header = OfHeader(classname=FieldClass.VectorField, name='genericObject')

def test_print_header() -> None:
    header = OfHeader(classname=FieldClass.VectorField, name='genericObject')
    expected_output = """\
version 2.0;
format ascii;
class volVectorField;
object genericObject;
"""
    assert str(header) == expected_output

def test_class_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(classname='VectorField', name='genericObject')
        #str(header)

def test_data_format_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(classname=FieldClass.VectorField, name='genericObject', format='ascii')
        #str(header)

def test_version_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(classname=FieldClass.VectorField, name='genericObject', version=2)
        #str(header)