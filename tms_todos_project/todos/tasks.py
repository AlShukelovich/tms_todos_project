import json
from time import sleep
from celery import shared_task
from django.forms import model_to_dict

from tms_todos_project.celery import app
from todos.models import Todo


@shared_task()
def logging_task(params=None):
    print(params)
    sleep(10)

@app.task
def create_todos():
    # loggin_data = Todo.objects.all()
    # loggin_data2 = model_to_dict(loggin_data)
    loggin_data2 = {'a':1, 'b':2, 'c':3}
    with open("todos_list.json", "w+") as new_file:
        for i in loggin_data2:
            json.dump(i, new_file)