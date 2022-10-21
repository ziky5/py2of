from ultimate_pyfoam.domain.of_dict import OfDict


def test_can_be_created() -> None:
    OfDict()


def test_data_can_be_accessed() -> None:
    a = OfDict({"FoamFile": {}})
    a.data


# def test_str_can_be_used():
#    str(OfDict(name="FoamFile", content={}))
#
#
# def test_str():
#    output = str(OfDict(name="FoamFile", content={"version": 2.0}))
#    string = """\
# FoamFile
# {
#    version 2.0;
# }\
# """
#    assert output == string
#
#
# def test_multiple_data_entries():
#    output = str(OfDict(name="FoamFile", content={"version": [2.0, 3.0]}))
#    string = """\
# FoamFile
# {
#    version 2.0 3.0;
# }\
# """
#    assert output == string
#
#
# def test_nested_of_dict():
#    # TODO :how do we want to use nested dicts?
#    string = """\
# solvers
# {
#    p
#    {
#        solver PCG;
#    }
# }\
# """
#    assert output == string
