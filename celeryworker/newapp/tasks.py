import os
import requests

from celery import shared_task
from sentry_sdk import capture_exception


@shared_task
def check_webpage():
    print(f"SENTRY_DSN: {os.getenv('SENTRY_DSN')}")
    try:
        response = requests.get("http://127.0.0.1:8001")
        if response.status_code != 200:
            raise Exception("Website is down, oh no!")
    except requests.exceptions.RequestException as e:
        capture_exception(e)
        # raise e
