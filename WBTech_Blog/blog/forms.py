from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    """
    Форма для создания объявления
    """
    #content = forms.CharField(widget=CKEditorWidget, label='Содержание объявления')
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
            'category': "Категория",
        }

        widgets = {'author': forms.HiddenInput()}