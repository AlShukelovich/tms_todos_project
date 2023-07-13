from django.shortcuts import render
from django.views.decorators.cache import cache_page

from todos.models import Todo

@cache_page(60*15)
def todo_from_db(request):
    list_todo_db = Todo.objects.all()
    return render(request, 'for_db.html', {'todos': list_todo_db})