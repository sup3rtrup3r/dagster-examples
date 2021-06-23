from dagster import pipeline
from zitarice.solids.custom_types import sort_by_calories_type, download_type_check_csv


@pipeline
def custom_type_pipeline():
    sort_by_calories_type(download_type_check_csv())
