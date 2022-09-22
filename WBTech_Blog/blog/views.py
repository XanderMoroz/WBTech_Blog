from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import PostForm
from rest_framework import viewsets
from .serializers import *
# Create your views here.

class AuthorList(ListView):

    model = Author
    template_name = 'author_list.html'
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
        return context

class AuthorDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному автору
    model = Author
    template_name = 'blog/author_detail.html'
    # Название объекта, в котором будет выбранный пользователем автор
    context_object_name = 'author_detail'


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить (Пост)
    model = Post
    # Поле, которое будет использоваться для сортировки постов
    ordering = '-creation_date'
    # Указываем имя шаблона, в котором будут все инструкции к показу постов
    template_name = 'blog/post_list.html'
    # Слово, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'all_post_list'


    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'

class PostCreate(CreateView, LoginRequiredMixin):
    """
    Класс представления для создания поста.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    model = Post
    template_name = 'blog/crud/create.html'
    form_class = PostForm

    def get_initial(self):
        """
        Переопределение функции для автозаполнения поля "автор поста"
        """
        initial = super().get_initial()
        user = self.request.user
        initial['author'] = user
        return initial

class PostUpdate(UpdateView, LoginRequiredMixin):
    template_name = 'blog/crud/edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView, LoginRequiredMixin):
    """
    Класс представления для удаления объявления.
    Наследован от встроенного дженерика.
    """
    template_name = 'blog/crud/delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

def subscribe(request, **kwargs):
    """Подписаться на автора"""
    author = Author.objects.get(pk=kwargs['pk'])
    user = request.user
    if user not in author.subscribers.all():
        author.subscribers.add(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def unsubscribe(request, **kwargs):
    """Отписаться от автора"""
    author = Author.objects.get(pk=kwargs['pk'])
    user = request.user
    if user in author.subscribers.all():
        author.subscribers.remove(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))



class UserPersonalPost(ListView, LoginRequiredMixin):
    """Лента пользователя"""
    model = Post
    ordering = '-creation_date'
    paginate_by = 10
    template_name = 'protect/account/user_account.html'
    context_object_name = 'all_post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        return context

def make_post_read(request, **kwargs):
    """Пометить пост как прочитанный"""
    current_post = Post.objects.get(pk=kwargs['pk'])
    current_user = request.user
    if current_user not in current_post.userread.all():
        current_post.userread.add(current_user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def make_post_unread(request, **kwargs):
    """Пометить пост как непрочитанный"""
    current_post = Post.objects.get(pk=kwargs['pk'])
    current_user = request.user
    if current_user in current_post.userread.all():
        current_post.userread.remove(current_user)
    return redirect(request.META.get('HTTP_REFERER', '/'))



class AuthorListAPI(viewsets.ModelViewSet):
    """Список всех авторов публикаций + создание автора"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPI(viewsets.ModelViewSet):
    """Детальная информация об авторах + редактирование и удаление автора"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostListAPI(viewsets.ModelViewSet):
    """Список всех публикаций + создание публикации"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPI(viewsets.ModelViewSet):
    """Детальная информация о публикации + редактирование и удаление публикации"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer