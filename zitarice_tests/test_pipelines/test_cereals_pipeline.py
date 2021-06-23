from dagster import execute_pipeline
from zitarice.pipelines.cereals_pipeline import hello_cereal_pipeline


def test_hello_cereal_pipeline():
    res = execute_pipeline(hello_cereal_pipeline)
    assert res.success
    assert len(res.result_for_solid("hello_cereal").output_value()) == 77
