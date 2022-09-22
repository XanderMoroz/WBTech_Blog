
from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    """
    Форма для создания объявления
    """
    class Meta:

        model = Post
        fields = [
            'title',
            'content',
            'author'
                ]
        labels = {
            'title': "Заголовок",
            'content': "Содержание",
        }

        widgets = {'author': forms.HiddenInput()}