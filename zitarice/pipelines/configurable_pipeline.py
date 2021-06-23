from dagster import pipeline, execute_pipeline
from zitarice.solids.caloriest_cereals import sort_by_calories
from zitarice.solids.configuring_download_csv import download_csv


@pipeline
def configurable_pipeline():
    sort_by_calories(download_csv())


if __name__ == '__main__':
    run_config = {
        "solids": {
            "download_csv": {
                "config": {"url": "https://docs.dagster.io/assets/cereal.csv"}
            }
        }
    }
    result = execute_pipeline(configurable_pipeline, run_config=run_config)
