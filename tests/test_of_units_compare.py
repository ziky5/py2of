from ultimate_pyfoam.domain.of_units import OfUnits as Of2
from ultimate_pyfoam.domain.of_units_re import OfUnitsRe as Of1


def test_are_methods_equivalent() -> None:
    a = Of1(SIunit="kg2m-3mol1")
    b = Of2(kg=2, m=-3, mol=1)
    assert str(a) == str(b)
