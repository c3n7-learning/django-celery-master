# https://docs.celeryq.dev/en/latest/userguide/canvas.html
from celery import chain
from dcelery.celery_config import app


@app.task(queue="tasks")
def add(x: float, y: float) -> float:
    return x + y


@app.task(queue="tasks")
def multiply(z):
    # Simulate an error for demonstration purposes
    if z == 5:
        raise ValueError("Division by zero.")
    return z * 2


def run_task_chain():
    task_chain = chain(add.s(2, 3), multiply.s())
    result = task_chain.apply_async()
    result.get()
