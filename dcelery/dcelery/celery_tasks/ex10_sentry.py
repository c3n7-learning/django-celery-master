from sentry_sdk import capture_exception
from dcelery.celery_config import app


@app.task(queue="tasks")
def divide_number_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        raise e
