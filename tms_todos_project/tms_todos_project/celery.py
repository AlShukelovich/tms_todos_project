import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tms_todos_project.settings")
app = Celery("tms_todos_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()