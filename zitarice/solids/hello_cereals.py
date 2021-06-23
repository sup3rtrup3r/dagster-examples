import requests
import csv
from dagster import solid


@solid
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")

    return cereals
