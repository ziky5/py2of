from ultimate_pyfoam.domain.of_units import OfUnits


def test_creatible() -> None:
    OfUnits()


def test_str_is_what_we_want() -> None:
    b = OfUnits(kg=2, mol=1)
    assert str(b) == "[2 0 0 0 1 0 0]"
