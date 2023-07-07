from django.contrib.auth.models import User
from .models import Todo


def create_initial_db():
    user_1 = User.objects.create_user(
        username='DMcI425',
        email='csouthey1d@instagram.com',
        password='12345',
        is_active=True
    )
    user_2 = User.objects.create_user(
        username='TJir522',
        email='msquelch22@hp.com',
        password='12345',
        is_active=True
    )
    user_3 = User.objects.create_user(
        username='THan878',
        email='sgailor3t@blogs.com',
        password='12345',
        is_active=True
    )


    Todo(
        title="todo1",
        description="do homework",
        user=user_1
    ).save()
    Todo(
        title="todo2",
        description="learn theory",
        user=user_2
    ).save()
    Todo(
        title="todo3",
        description="clean up at home",
        user=user_2
    ).save()
    Todo(
        title="todo4",
        description="go for a walk",
        user=user_3
    ).save()
    Todo(
        title="todo5",
        description="go to work",
        user=user_1
    ).save()
    Todo(
        title="todo6",
        description="go shopping",
        user=user_2
    ).save()
    Todo(
        title="todo7",
        description="learn english",
        user=user_3
    ).save()
    Todo(
        title="todo8",
        description="learn German",
        user=user_1
    ).save()