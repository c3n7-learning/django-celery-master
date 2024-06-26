from celery import shared_task
from django.core.management import call_command
import time


@shared_task(queue="tasks")
def management_command():
    call_command("test_command")


# @shared_task(task_rate_limit="2/m")
# def tp1(queue="celery"):
#     time.sleep(3)
#     return


# @shared_task
# def tp2(queue="celery:1"):
#     time.sleep(3)
#     return


# @shared_task
# def tp3(queue="celery:2"):
#     time.sleep(3)
#     return


# @shared_task
# def tp4(queue="celery:3"):
#     time.sleep(3)
#     return
