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
    with open("todos_list.txt", "w") as new_file:
        dict_from_db = [todo for todo in Todo.objects.values_list('user', 'title').order_by('user').filter(copmlete__exact=1)]
        for i in dict_from_db:
            new_file.write(str(i))
        new_file.close()

@app.task
def create_todos_json():
    with open(f"todos_list.json", "w+") as new_file:
        dict_from_db = [model_to_dict(todo) for todo in Todo.objects.filter(title__exact='todo2')]
        json.dump(str(dict_from_db), new_file)