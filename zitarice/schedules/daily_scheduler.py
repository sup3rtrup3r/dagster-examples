from dagster import daily_schedule
from datetime import datetime, time


def weekday_filter(_context):
    weekno = datetime.today().weekday()
    # Returns true if current day is a weekday
    return weekno < 5


@daily_schedule(
    pipeline_name="complex_pipeline",
    start_date=datetime(2021, 6, 23),
    execution_time=time(10, 9),
    execution_timezone="CET",
    should_execute=weekday_filter,
)
def good_morning_schedule(date):
    return {
        "solids": {
            "hello_cereal": {
                "inputs": {"date": {"value": date.strftime("%Y-%m-%d")}}
            }
        }
    }
