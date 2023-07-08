from django.urls import path, include
from rest_framework import routers
from todos.views.api_for_serializers import TodoViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]