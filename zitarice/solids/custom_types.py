import requests
import csv

from dagster import solid, DagsterType, OutputDefinition, InputDefinition, TypeCheck


def is_list_of_dicts(_, value):
    return isinstance(value, list) and all(
        isinstance(element, dict) for element in value
    )


def less_simple_data_frame_type_check(_, value):
    if not isinstance(value, list):
        return TypeCheck(
            success=False,
            description=f"LessSimpleDataFrame should be a list of dicts, got {type(value)}",
        )

    fields = [field for field in value[0].keys()]

    for i in range(len(value)):
        row = value[i]
        idx = i + 1
        if not isinstance(row, dict):
            return TypeCheck(
                success=False,
                description=(
                    f"LessSimpleDataFrame should be a list of dicts, got {type(row)} for row {idx}"
                ),
            )
        row_fields = [field for field in row.keys()]
        if fields != row_fields:
            return TypeCheck(
                success=False,
                description=(
                    f"Rows in LessSimpleDataFrame should have the same fields, got {row_fields} "
                    f"for row {idx}, expected {fields}"
                ),
            )

    return TypeCheck(
        success=True,
        description="LessSimpleDataFrame summary statistics",
        metadata={
            "n_rows": len(value),
            "n_cols": len(value[0].keys()) if len(value) > 0 else 0,
            "column_names": str(
                list(value[0].keys()) if len(value) > 0 else []
            ),
        },
    )


SimpleDataFrame = DagsterType(
    name="SimpleDataFrame",
    type_check_fn=less_simple_data_frame_type_check,
    description="A naive representation of a data frame, e.g., as returned by csv.DictReader.",
)


@solid(output_defs=[OutputDefinition(SimpleDataFrame)])
def download_type_check_csv(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    context.log.info("Read {n_lines} lines".format(n_lines=len(lines)))
    return [row for row in csv.DictReader(lines)]


@solid(input_defs=[InputDefinition("cereals", SimpleDataFrame)])
def sort_by_calories_type(context, cereals):
    sorted_cereals = sorted(cereals, key=lambda cereal: cereal["calories"])
    context.log.info(f'Most caloric cereal: {sorted_cereals[-1]}["name"]')
