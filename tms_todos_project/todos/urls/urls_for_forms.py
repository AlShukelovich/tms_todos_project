from django.urls import path, include
from todos import views

from todos.views.api_for_forms import todo_dict_from_db
from todos.views.api_for_forms import todo


urlpatterns = [
    path('api_forms/', views.api_for_forms.todo_dict_from_db),
    path('<int:todo_id>/', views.api_for_forms.todo),
]