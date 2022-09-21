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
        return context

class AuthorDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Author
    # Используем другой шаблон — product.html
    template_name = 'blog/author_detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'author_detail'


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить (Объявление)
    model = Post
    # Поле, которое будет использоваться для сортировки объявлений
    ordering = '-creation_date'
    # Указываем имя шаблона, в котором будут все инструкции к показу объявлений
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
    Класс представления для создания объявления.
    Наследован от встроенного дженерика, миксина требующего авторизацию и миксина, требующего право доступа
    """
    model = Post
    template_name = 'blog/crud/create.html'
    form_class = PostForm

    def get_initial(self):
        """
        Переопределение функции для автозаполнения поля "автор объявления"
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
    author = Author.objects.get(pk=kwargs['pk'])
    user = request.user
    if user not in author.subscribers.all():
        author.subscribers.add(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

def unsubscribe(request, **kwargs):
    author = Author.objects.get(pk=kwargs['pk'])
    user = request.user
    if user in author.subscribers.all():
        author.subscribers.remove(user)
    return redirect(request.META.get('HTTP_REFERER', '/'))


class UserPersonalPost(ListView, LoginRequiredMixin):
    model = Post
    ordering = '-creation_date'
    template_name = 'protect/account/user_account.html'
    context_object_name = 'all_post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        current_user = self.request.user
        # user_subscribed = UserSubscribers.objects.filter(subscribers=current_user)
        # lovely_authors = user_subscribed.user.all #Author.objects.filter(usersubscribers=user)
        # lovely_posts = Post.objects.filter(author=lovely_authors)
        # user_unread = Post.objects.filter(status='UNREAD')

        #context['post_unread'] = user_unread
        # context['user_ads'] = user.advertisement_set.all
        # user_feedbacks = Feedback.objects.filter(ad__user=user)
        # context['user_feedbacks'] = user_feedbacks
        # accepted_feedbacks = user_feedbacks.filter(acception=True)
        # context['accepted_feedbacks'] = accepted_feedbacks
        # вписываем наш фильтр (AdFilter) в контекст
        #context['filter'] = UserLovelyPostFilter(self.request.GET, queryset=Post.objects.all)
        return context



# Create your views here.

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