from ultimate_pyfoam.domain.of_units import OF_units

def test_creatible():
    OF_units()

def test_str_is_what_we_want():
    b = OF_units(kg = 2, mol = 1)
    assert str(b) == '[2 0 0 0 1 0 0]'