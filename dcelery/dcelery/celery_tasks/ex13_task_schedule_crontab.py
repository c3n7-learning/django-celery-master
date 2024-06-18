"""
*    *    *    *    *  command to be executed
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)

"""

from dcelery.celery_config import app
from datetime import timedelta
from celery.schedules import crontab

# app.conf.beat_schedule = {
#     "task1": {
#         "task": "dcelery.celery_tasks.ex13_task_schedule_crontab.task1",
#         "schedule": crontab(
#             # minute="0-59/10", hour="15-23", day_of_week="tue"
#         ),
#         "kwargs": {"message": "bar"},
#         "args": (1, 2),
#         "options": {
#             "queue": "tasks",
#             "priority": 5,
#         },
#     },
#     "task2": {
#         "task": "dcelery.celery_tasks.ex13_task_schedule_crontab.task2",
#         "schedule": timedelta(seconds=10),
#     },
# }


@app.task(queue="tasks")
def task1(a, b, **kwargs):
    result = a + b
    print(f"Running task 1: result ({result})")


@app.task(queue="tasks")
def task2():
    print("Running task 2")
