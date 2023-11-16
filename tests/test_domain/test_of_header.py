import pytest

from py2of.domain.of_header import OfHeader, FieldType, DataFormat


def test_create_header() -> None:
    header = OfHeader(classname=FieldType.VectorField, name="genericObject")


def test_print_header_dictionary() -> None:
    header = OfHeader(classname=FieldType.Dictionary, name="genericObject")
    expected_output = """\
version 2.0;
format ascii;
class dictionary;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_scalar_field() -> None:
    header = OfHeader(classname=FieldType.ScalarField, name="genericObject")
    expected_output = """\
version 2.0;
format ascii;
class volScalarField;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_vector_field() -> None:
    header = OfHeader(classname=FieldType.VectorField, name="genericObject")
    expected_output = """\
version 2.0;
format ascii;
class volVectorField;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_tensor_field() -> None:
    header = OfHeader(classname=FieldType.TensorField, name="genericObject")
    expected_output = """\
version 2.0;
format ascii;
class volTensorField;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_regioobject() -> None:
    header = OfHeader(classname=FieldType.RegIOObject, name="genericObject")
    expected_output = """\
version 2.0;
format ascii;
class regIOobject;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_binary_format() -> None:
    header = OfHeader(
        classname=FieldType.VectorField, name="genericObject", format=DataFormat.Binary
    )
    expected_output = """\
version 2.0;
format binary;
class volVectorField;
object genericObject;
"""
    assert str(header) == expected_output


def test_print_header_nondefault_version() -> None:
    header = OfHeader(
        classname=FieldType.VectorField, name="genericObject", version=1.5
    )
    expected_output = """\
version 1.5;
format ascii;
class volVectorField;
object genericObject;
"""
    assert str(header) == expected_output


def test_class_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(classname="VectorField", name="genericObject")


def test_data_format_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(
            classname=FieldType.VectorField, name="genericObject", format="ascii"
        )


def test_version_type() -> None:
    with pytest.raises(AssertionError):
        header = OfHeader(
            classname=FieldType.VectorField, name="genericObject", version=2
        )
