from django.urls import path, include
from rest_framework import routers
from todos.views.api_for_serializers import TodoViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todo_cache/', TodoListViewSet.as_view()),
]