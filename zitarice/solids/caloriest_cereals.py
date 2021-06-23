from dagster import solid


@solid
def find_highest_calorie_cereal(cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["calories"])
    )
    return sorted_cereals[-1]["name"]


@solid
def sort_by_calories(context, cereals):
    sorted_cereals = sorted(
        cereals, key=lambda cereal: int(cereal["calories"])
    )

    context.log.info(f'Most caloric cereal: {sorted_cereals[-1]["name"]}')
