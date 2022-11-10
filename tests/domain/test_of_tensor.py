from ultimate_pyfoam.domain.of_tensor import OfTensor


def test_create_tensor() -> None:
    OfTensor(xx=1, xy=0, xz=0, yx=0, yy=1, yz=0, zx=0, zy=0, zz=1)


def test_tensor_to_str() -> None:
    string = str(OfTensor(xx=1, xy=0, xz=0, yx=0, yy=1, yz=0, zx=0, zy=0, zz=1))

    assert (
        string
        == """\
(
    1 0 0
    0 1 0
    0 0 1
)\
"""
    )
