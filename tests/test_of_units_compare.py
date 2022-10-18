from ultimate_pyfoam.domain.of_units_re import OF_units as OF1
from ultimate_pyfoam.domain.of_units import OF_units as OF2

def test_are_methods_equivalent():
    a = OF1(SIunit='kg2m-3mol1')
    b = OF2(kg=2,m=-3,mol=1)
    assert str(a) == str(b)