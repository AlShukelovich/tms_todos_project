from django.shortcuts import render
from todos.models import Todo


def todo_from_db(request):
    list_todo_db = Todo.objects.all()
    return render(request, 'for_db.html', {'todos': list_todo_db})