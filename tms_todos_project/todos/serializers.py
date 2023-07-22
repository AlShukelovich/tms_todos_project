from django.contrib.auth.models import User

from .models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Todo
        fields = (
            "id", 'title', 'description', 'user', 'copmlete', 'created_at'
        )