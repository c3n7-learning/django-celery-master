from celery import group
from dcelery.celery_config import app

app.conf.task_acks_late = True
app.conf.task_reject_worker_on_lost = True


@app.task(queue="tasks")
def my_task(z):
    try:
        if z == 2:
            raise ValueError("Wrong Number")
    except Exception as e:
        handle_failed_task.apply_async(
            args=(
                z,
                str(e),
            )
        )
        raise


@app.task(queue="dead_letter")
def handle_failed_task(z, exception):
    return "Custom logic to process"


def run_group():
    task_group = group(
        my_task.s(1),
        my_task.s(2),
        my_task.s(3),
    )
    task_group.apply_async()
