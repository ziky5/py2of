from ultimate_pyfoam.domain.of_units import OF_units

def test_creatible():
    OF_units(SIunit='Newton')

def test_str():
    a = OF_units(SIunit='Newton')
    str(a)