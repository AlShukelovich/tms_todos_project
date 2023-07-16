from django.shortcuts import render
from django.views.decorators.cache import cache_page

from todos.models import Todo
from todos.tasks import logging_task

#@cache_page(5)#(60*15)
def todo_from_db(request):
    list_todo_db = Todo.objects.all()
    logging_task.delay(params=["Todos function called"])
    return render(request, 'for_db.html', {'todos': list_todo_db})