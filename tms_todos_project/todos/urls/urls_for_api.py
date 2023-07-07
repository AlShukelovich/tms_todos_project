from django.urls import path, include
from todos import views
from todos.views.api import todo_from_db


urlpatterns = [
    path('api/', views.api.todo_from_db, name="for_db"),
]