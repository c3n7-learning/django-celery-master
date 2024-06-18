import os

# from sentry_sdk.integrations.celery import CeleryIntegration
from celery import Celery
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        queue_arguments={"x-max-priority": 10},
    ),
    Queue(
        "dead_letter",
        routing_key="dead_letter",
    ),
]


app.conf.task_acks_late = True
app.conf.task_default_priority = 5
# https://docs.celeryq.dev/en/stable/userguide/configuration.html#worker-prefetch-multiplier
# Select tasks 1 by 1
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "dcelery", "celery_tasks")

if os.path.exists(task_folder) and os.path.isdir(task_folder):
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex13") and filename.endswith(".py"):
            # -3 to remove the .py
            module_name = f"dcelery.celery_tasks.{filename[:-3]}"

            # dynamically import the module
            module = __import__(module_name, fromlist=["*"])

            # get all the functions in the imported module
            for name in dir(module):
                obj = getattr(module, name)
                # if the function name starts with "my_task"
                # if callable(obj) and name.startswith("my_task"):
                if callable(obj):
                    task_modules.append(f"{module_name}.{name}")

    print(f"[INFO] Importing tasks {task_modules}")
    app.autodiscover_tasks(task_modules)
