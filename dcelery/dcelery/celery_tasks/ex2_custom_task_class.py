import logging
from celery import Task
from dcelery.celery_config import app

logging.basicConfig(
    # filename='app.log'
    level=logging.ERROR,
    format="%(actime)s %(levelname)s %(message)s",
)


class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("CustomTask::Connection Error")
        else:
            print("{0!r} failed: {1!r}".format(task_id, exc))


app.Task = CustomTask


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection error occurred...")
    except ConnectionError:
        logging.error("Connection Error...")
        raise ConnectionError()
