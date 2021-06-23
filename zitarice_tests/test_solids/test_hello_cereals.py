from dagster import execute_solid
from zitarice.solids.hello_cereals import hello_cereal


def test_hello_cereal_solid():
    res = execute_solid(hello_cereal)
    assert res.success
    assert len(res.output_value()) == 77
