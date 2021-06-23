from dagster import solid


@solid
def find_sugariest(context, cereals):
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    context.log.info(f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')


@solid
def find_sugariest_cereal(cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["sugars"])
    )
    return sorted_cereals[-1]["name"]
