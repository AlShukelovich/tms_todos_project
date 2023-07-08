from django.forms import model_to_dict
from django.http import JsonResponse

from todos.forms import TodoForm, TodoUpdateForm
from todos.models import Todo


def todo_dict_from_db(request):
    if request.method == "POST":
       form = TodoForm(request.POST)
       if form.is_valid():
          data = form.save()
          return JsonResponse(model_to_dict(data))
       else:
          return JsonResponse({'status': 400, 'errors': form.errors})
    dict_from_db = [model_to_dict(todo) for todo in Todo.objects.all()]
    return JsonResponse({'todos': dict_from_db})


def todo(request, todo_id: int):
    try:
        post_obj = Todo.objects.get(id=todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Todo not found.'})

    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=post_obj)
        if form.is_valid():
            data = form.save()
            return JsonResponse(model_to_dict(data))
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})

    elif request.method == 'DELETE':
        post_obj.delete()
        return JsonResponse({'status': 204, 'message': 'Todo successfully deleted'})

    return JsonResponse({'todo': model_to_dict(post_obj)})