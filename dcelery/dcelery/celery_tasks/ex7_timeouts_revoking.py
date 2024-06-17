from dcelery.celery_config import app
from time import sleep


@app.task(queue="tasks", time_limit=5)
def my_task_long_running():
    sleep(6)
    return "Task completed successfully"
