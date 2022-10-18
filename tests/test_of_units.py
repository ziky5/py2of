from ultimate_pyfoam.domain.of_units import OF_units

def test_creatible():
    OF_units(SIunit='kgm-1s-2')

def test_units():
    a = OF_units(SIunit='kgm-1s-2')
    assert type(OF_units.values) is list

#def test_str():
#    a = OF_units(SIunit='kg2')
#    str(a)

def test_str_is_what_we_want():
    b = OF_units(SIunit='kg2cd1')
    assert str(b) == '[ 2 0 0 0 0 0 1]'

#m a mol nejsou stejne