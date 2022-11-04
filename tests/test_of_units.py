from ultimate_pyfoam.domain.of_units import OfUnits


def test_creatible() -> None:
    OfUnits()


def test_str() -> None:
    b = OfUnits(kg=2, mol=1, s=5, cd=-3, A=-2, m=0, K=13)
    assert str(b) == "[2 0 5 13 1 -2 -3]"


def test_default_zeros() -> None:
    b = OfUnits(kg=2, mol=1)
    assert str(b) == "[2 0 0 0 1 0 0]"
