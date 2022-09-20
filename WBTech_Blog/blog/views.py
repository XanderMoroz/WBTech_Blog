from django.shortcuts import render

# Create your views here.
from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Post

class AuthorList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Author
    template_name = 'author_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'author_list'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context

class AuthorDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Author
    # Используем другой шаблон — product.html
    template_name = 'blog/author_detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'author_detail'
