import csv

import requests
from dagster import solid


@solid
def download_cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]
