from django import forms
from .models import Task, TaskType, Comment

class TypeForm(forms.ModelForm):
    class Meta:
        model=Type
        fields='__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'
