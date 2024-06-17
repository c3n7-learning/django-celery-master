from dcelery.celery_config import app
import logging

logging.basicConfig(
    # filename='app.log'
    level=logging.ERROR,
    format="%(actime)s %(levelname)s %(message)s",
)


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection error occurred...")
    except ConnectionError:
        logging.error("Connection Error...")
        raise ConnectionError()
