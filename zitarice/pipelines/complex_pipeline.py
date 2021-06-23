from dagster import solid, pipeline

from zitarice.solids.download_cereals_csv import download_cereals
from zitarice.solids.caloriest_cereals import find_highest_calorie_cereal
from zitarice.solids.proteinest_cereals import find_highest_protein_cereal
from zitarice.solids.sugariest_cereal import find_sugariest_cereal


@solid
def display_results(context, most_calories, most_protein, most_sugar):
    context.log.info(f'Most caloric cereal: {most_calories}')
    context.log.info(f'Most protein-rich cereal: {most_protein}')
    context.log.info(f'Most sugar cereal: {most_sugar}')


@pipeline
def complex_pipeline():
    cereals = download_cereals()
    display_results(
        most_calories=find_highest_calorie_cereal(cereals),
        most_protein=find_highest_protein_cereal(cereals),
        most_sugar=find_sugariest_cereal(cereals),
    )
