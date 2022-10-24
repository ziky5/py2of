from ultimate_pyfoam.domain.of_units_re import OfUnitsRe


def test_creatible() -> None:
    OfUnitsRe(SIunit="kgm-1s-2")


def test_units() -> None:
    a = OfUnitsRe(SIunit="kgm-1s-2")
    assert type(a.unit()) is list


def test_str() -> None:
    c = OfUnitsRe(SIunit="kg2")
    assert type(c.SIunit) is str


def test_str_is_what_we_want() -> None:
    b = OfUnitsRe(SIunit="kg2m-3mol1")
    assert str(b) == "[2 -3 0 0 1 0 0]"


# m a mol nejsou stejne
