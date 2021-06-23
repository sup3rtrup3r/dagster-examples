from zitarice.solids.hello_cereals import hello_cereal
from dagster import pipeline
from dagster import execute_pipeline


@pipeline
def hello_cereal_pipeline():
    hello_cereal()


if __name__ == "__main__":
    result = execute_pipeline(hello_cereal_pipeline)
