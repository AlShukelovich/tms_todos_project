import datetime

from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    copmlete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now())
