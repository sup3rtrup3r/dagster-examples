from datetime import datetime

from dagster import hourly_schedule


@hourly_schedule(
    pipeline_name="my_pipeline",
    start_date=datetime(2021, 6, 21),
    execution_timezone="CET",
)
def my_hourly_schedule(_context):
    """
    A schedule definition. This example schedule runs a pipeline every hour.

    For more hints on scheduling pipeline runs in Dagster, see our documentation overview on
    Schedules:
    https://docs.dagster.io/overview/schedules-sensors/schedules
    """
    run_config = {}
    return run_config
