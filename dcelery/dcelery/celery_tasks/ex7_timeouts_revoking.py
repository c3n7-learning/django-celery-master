from dcelery.celery_config import app
from time import sleep


@app.task(queue="tasks", time_limit=10)
def my_task_long_running():
    sleep(6)
    return "Task completed successfully"


def execute_tasks():
    result = my_task_long_running.delay()
    try:
        task_result = result.get(timeout=40)
    except TimeoutError:
        print("Task timed out")

    task = my_task_long_running.delay()
    task.revoke(terminate=True)

    # Sleep for a bit, we want the revokation to be processed
    sleep(3)
    print(f"Task Status: {task.status}")
