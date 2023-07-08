from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Todo


class TodoForm(forms.ModelForm):
    copmlete = forms.BooleanField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'user', 'copmlete']


    def clean_description(self):
        if len(self.cleaned_data.get("description")) < 1:
            raise ValidationError('Value must be more than 1 character.')
        return self.cleaned_data.get("description")


class TodoUpdateForm(TodoForm):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    copmlete = forms.BooleanField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'description', 'user', 'copmlete']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data.get('title') or self.instance.title
        cleaned_data['description'] = cleaned_data.get('description') or self.instance.description
        cleaned_data['user'] = cleaned_data.get('user') or self.instance.user
        cleaned_data.get('copmlete') if cleaned_data.get('copmlete') is not None else self.instance.copmlete


class PostFilterForm(forms.Form):
    title = forms.CharField(required=False)