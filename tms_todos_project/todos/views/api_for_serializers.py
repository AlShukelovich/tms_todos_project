from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
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


class TodoListViewSet(APIView):
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format=None):
        content = {

        }
        return Response(content)