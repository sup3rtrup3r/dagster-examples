from dagster import pipeline

from zitarice.solids.sugariest_cereal import find_sugariest
from zitarice.solids.download_cereals_csv import download_cereals


@pipeline
def serial_pipeline():
    find_sugariest(download_cereals())
