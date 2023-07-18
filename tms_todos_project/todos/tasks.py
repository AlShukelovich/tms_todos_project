import json
from time import sleep
from celery import shared_task
from django.forms import model_to_dict

from tms_todos_project.celery import app
#from tms_todos_project.celery import app
#from tms_todos_project.tms_todos_project.celery import app
from todos.models import Todo
from todos.serializers import TodoSerializer


@shared_task()
def logging_task(params=None):
    print(params)
    sleep(10)


@app.task
def create_todos():
    with open("todos_list.json", "w+") as new_file:
        dict_from_db = [model_to_dict(todo) for todo in Todo.objects.filter(title__exact='todo2')]
        json.dump(dict_from_db, new_file)
