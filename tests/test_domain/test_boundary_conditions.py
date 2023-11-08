from py2of.domain.of_boundary_conditions import FixedValue, ZeroGradient
from py2of.domain.of_file import OfFile
from py2of.domain.of_list import NonUniformList, UniformList
from py2of.domain.of_vector import OfVector


def unify_value(value):
    return value.replace("\n", "").replace("\t", "").replace(" ", "")


def test_fixed_value_uniform_value_scalar():
    fv = FixedValue(UniformList(0))
    assert fv() == {"type": "fixedValue", "value": "uniform 0"}


def test_fixed_value_uniform_value_vector():
    fv = FixedValue(UniformList(OfVector([0, 0, 0])))
    assert fv() == {"type": "fixedValue", "value": "uniform (0 0 0)"}


def test_zero_gradient():
    zg = ZeroGradient()
    assert zg() == {"type": "zeroGradient"}


def test_fixed_value_nonuniform_value_scalar():
    fv = FixedValue(NonUniformList([1, 2]))
    bc = fv()
    bc["value"] = unify_value(bc["value"])
    should_be = {
        "type": "fixedValue",
        "value": unify_value("nonuniform List<scalar> 2(1 2);"),
    }
    assert bc == should_be


def test_boundary_field():
    of_file = OfFile(
        {"boundaryField": {"movingWall": FixedValue(UniformList(OfVector([1, 0, 0])))}}
    )

    should_be = """\
boundaryField
{
    movingWall
    {
        type fixedValue;
        value uniform (1 0 0);
    }
}
"""

    assert str(of_file) == should_be
