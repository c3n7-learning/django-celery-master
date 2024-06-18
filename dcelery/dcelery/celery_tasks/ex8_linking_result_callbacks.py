from dcelery.celery_config import app
import sys


@app.task(queue="tasks")
def my_task():
    raise ValueError("Something went wrong.")
    # pass


@app.task(queue="tasks")
def my_task_process_result(result):
    sys.stdout.write(f"Process task results\n")
    sys.stdout.flush()


@app.task(queue="tasks")
def my_task_error_handler(task_id, exc, traceback):
    sys.stdout.write(f">>>>")
    sys.stdout.write(str(exc))
    sys.stdout.write(f">>>>")
    sys.stdout.flush()


def run_task():
    my_task.apply_async(
        link=[
            my_task_process_result.s(),
        ],
        link_error=[my_task_error_handler.s()],
    )
