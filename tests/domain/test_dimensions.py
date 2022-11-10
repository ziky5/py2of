from ultimate_pyfoam.domain.dimensions import Dimensions


def test_creatable() -> None:
    Dimensions()


def test_str() -> None:
    output = str(Dimensions(kg=2, mol=1, s=5, cd=-3, A=-2, m=0, K=13))
    assert output == "[2 0 5 13 1 -2 -3]"


def test_default_zeros() -> None:
    output = str(Dimensions(kg=2, mol=1))
    assert output == "[2 0 0 0 1 0 0]"


def test_no_keywords() -> None:
    output = str(Dimensions(0, 2, -1, 0, 0, 0, 0))
    assert output == "[0 2 -1 0 0 0 0]"
