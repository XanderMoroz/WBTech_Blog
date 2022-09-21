from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #postCount = models.IntegerField(default=0)
    subscribers = models.ManyToManyField(User, through='UserSubscribers', related_name='author_subscribers')

    def __str__(self):
        return f'{self.user}'

class Post(models.Model):
    '''
    Эта модель описывает пост, которые создают пользователи.
    Пост состоят из заголовка и текста.
    Каждое объявление относится к одной из следующих категорий:
    - поле связанное с пользователем(автором объявления);
    - автоматически добавляемая дата и время создания объявления;
    - заголовок объявления;
    - текст объявления.
    '''
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор объявления')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(max_length=256, verbose_name='Содержание')
    status = models.CharField(max_length=6, choices=[('UNREAD', 'Непрочитанный'), ('READ', 'Прочитанный')], default='UNREAD',
                                verbose_name='Статус')

    def __str__(self):
        return f'{self.title} {self.author}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/posts/{self.id}'

class UserSubscribers(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    subscribers = models.ForeignKey(User, on_delete=models.CASCADE)
