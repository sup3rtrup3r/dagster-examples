from dagster import repository

from zitarice.pipelines.my_pipeline import my_pipeline
from zitarice.pipelines.cereals_pipeline import hello_cereal_pipeline
from zitarice.pipelines.serial_pipeline import serial_pipeline
from zitarice.pipelines.complex_pipeline import complex_pipeline
from zitarice.pipelines.configurable_pipeline import configurable_pipeline
from zitarice.pipelines.custom_types_pipeline import custom_type_pipeline
from zitarice.solids.modes import modes_pipeline

from zitarice.schedules.my_hourly_schedule import my_hourly_schedule
from zitarice.schedules.daily_scheduler import good_morning_schedule

from zitarice.sensors.my_sensor import my_sensor


@repository
def zitarice():
    """
    The repository definition for this zitarice Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    pipelines = [my_pipeline, hello_cereal_pipeline, serial_pipeline,
                 complex_pipeline, configurable_pipeline, custom_type_pipeline, modes_pipeline]
    schedules = [my_hourly_schedule, good_morning_schedule]
    sensors = [my_sensor]

    return pipelines + schedules + sensors
