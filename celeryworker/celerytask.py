from celery import Celery
import sentry_sdk
from datetime import timedelta
import os

app = Celery("task")
app.config_from_object("celeryconfig")
app.conf.imports = "newapp.tasks"

app.autodiscover_tasks()

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app.conf.beat_schedule = {
    "task1": {
        "task": "newapp.tasks.check_webpage",
        "schedule": timedelta(seconds=10),
    }
}
