from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = ['id', 'title', 'description', 'user', 'copmlete']
    filterset_fields = ['id', 'title', 'description', 'user']
    search_fields = ['id', 'title', 'description']