import pytest

from py2of.domain.of_field import OfField, UniformList, NonUniformList
from py2of.domain.dimensions import Dimensions
from py2of.domain.of_list import OfList
from py2of.domain.of_vector import OfVector
from py2of.domain.of_tensor import OfTensor
from py2of.domain.of_file import OfFile


def test_create_field() -> None:
    OfField(
        fieldName="genericObject",
        dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
        internalData=NonUniformList(
            [
                OfVector(x=1, y=2, z=3),
                OfVector(x=0.5, y=1.5, z=2.5),
                OfVector(x=3, y=6.2, z=0.5),
            ],
        ),
        boundaryData=OfFile(
            {
                "BC_wall": {"type": "zeroGradient"},
                "BC_inlet": {"type": "zeroGradient"},
            }
        ),
    )


def test_print_scalar_field() -> None:
    field = OfField(
        fieldName="genericObject",
        dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
        internalData=NonUniformList([0.5, 1.5, 2.5]),
        boundaryData=OfFile(
            {
                "BC_wall": {"type": "zeroGradient"},
                "BC_inlet": {"type": "zeroGradient"},
            }
        ),
    )
    expected_output = """\
FoamFile
{
    version 2.0;
    format ascii;
    class volScalarField;
    object genericObject;
}
dimensions [1 2 -1 -2 3 4 9];
internalField nonuniform\tList<scalar>
3
(
0.5
1.5
2.5
);
boundaryField
{
    BC_wall
    {
        type zeroGradient;
    }
    BC_inlet
    {
        type zeroGradient;
    }
}
"""
    assert str(field) == expected_output


def test_print_vector_field() -> None:
    field = OfField(
        fieldName="genericObject",
        dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
        internalData=NonUniformList(
            [
                OfVector(x=1, y=2, z=3),
                OfVector(x=0.5, y=1.5, z=2.5),
                OfVector(x=3, y=6.2, z=0.5),
            ],
        ),
        boundaryData=OfFile(
            {
                "BC_wall": {"type": "zeroGradient"},
                "BC_inlet": {"type": "zeroGradient"},
            }
        ),
    )
    expected_output = """\
FoamFile
{
    version 2.0;
    format ascii;
    class volVectorField;
    object genericObject;
}
dimensions [1 2 -1 -2 3 4 9];
internalField nonuniform\tList<vector>
3
(
(1 2 3)
(0.5 1.5 2.5)
(3 6.2 0.5)
);
boundaryField
{
    BC_wall
    {
        type zeroGradient;
    }
    BC_inlet
    {
        type zeroGradient;
    }
}
"""
    assert str(field) == expected_output


def test_print_tensor_field() -> None:
    field = OfField(
        fieldName="genericObject",
        dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
        internalData=NonUniformList(
            [
                OfTensor(xx=1, xy=2, xz=3, yx=4, yy=5, yz=6, zx=7, zy=8, zz=9),
                OfTensor(
                    xx=0.1,
                    xy=3.1,
                    xz=4.8,
                    yx=5.0,
                    yy=12.1,
                    yz=3.3,
                    zx=9.0,
                    zy=8.7,
                    zz=0.0,
                ),
            ],
        ),
        boundaryData=OfFile(
            {
                "BC_wall": {"type": "zeroGradient"},
                "BC_inlet": {"type": "zeroGradient"},
            }
        ),
    )
    expected_output = """\
FoamFile
{
    version 2.0;
    format ascii;
    class volTensorField;
    object genericObject;
}
dimensions [1 2 -1 -2 3 4 9];
internalField nonuniform\tList<tensor>
2
(
(
    1 2 3
    4 5 6
    7 8 9
)
(
    0.1 3.1 4.8
    5.0 12.1 3.3
    9.0 8.7 0.0
)
);
boundaryField
{
    BC_wall
    {
        type zeroGradient;
    }
    BC_inlet
    {
        type zeroGradient;
    }
}
"""
    assert str(field) == expected_output


def test_fieldname_type() -> None:
    with pytest.raises(AssertionError):
        field = OfField(
            fieldName=1,
            dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
            internalData=NonUniformList(
                [
                    OfVector(x=1, y=2, z=3),
                    OfVector(x=0.5, y=1.5, z=2.5),
                    OfVector(x=3, y=6.2, z=0.5),
                ],
            ),
            boundaryData=OfFile(
                {
                    "BC_wall": {"type": "zeroGradient"},
                    "BC_inlet": {"type": "zeroGradient"},
                }
            ),
        )


def test_dimensions_type() -> None:
    with pytest.raises(AssertionError):
        field = OfField(
            fieldName="genericObject",
            dimensions=[1, 2, -1, -2, 3, 4, 9],
            internalData=OfList(
                "nonuniform",
                [
                    OfVector(x=1, y=2, z=3),
                    OfVector(x=0.5, y=1.5, z=2.5),
                    OfVector(x=3, y=6.2, z=0.5),
                ],
            ),
            boundaryData=OfFile(
                {
                    "BC_wall": {"type": "zeroGradient"},
                    "BC_inlet": {"type": "zeroGradient"},
                }
            ),
        )


def test_internalField_type() -> None:
    with pytest.raises(AssertionError):
        field = OfField(
            fieldName="genericObject",
            dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
            internalData=[[1, 2, 3], [0.5, 1.5, 2.5], [3, 6.2, 0.5]],
            boundaryData=OfFile(
                {
                    "BC_wall": {"type": "zeroGradient"},
                    "BC_inlet": {"type": "zeroGradient"},
                }
            ),
        )


def test_boundaryField_type() -> None:
    with pytest.raises(AssertionError):
        field = OfField(
            fieldName="genericObject",
            dimensions=Dimensions(kg=1, m=2, s=-1, K=-2, mol=3, A=4, cd=9),
            internalData=OfList(
                "nonuniform",
                [
                    OfVector(x=1, y=2, z=3),
                    OfVector(x=0.5, y=1.5, z=2.5),
                    OfVector(x=3, y=6.2, z=0.5),
                ],
            ),
            boundaryData={
                "BC_wall": {"type": "zeroGradient"},
                "BC_inlet": {"type": "zeroGradient"},
            },
        )
