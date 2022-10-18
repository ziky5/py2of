from ultimate_pyfoam.domain.of_units import OF_units

def test_creatible():
    OF_units(SIunit='kgm-1s-2')

def test_units():
    a = OF_units(SIunit='kgm-1s-2')
    assert type(a.values) is list

def test_str():
    A = OF_units(SIunit='kg2')
    assert type(A.SIunit) is str

def test_str_is_what_we_want():
    b = OF_units(SIunit='kg2mol1')
    assert str(b) == '[2 0 0 0 1 0 0]'

#m a mol nejsou stejne