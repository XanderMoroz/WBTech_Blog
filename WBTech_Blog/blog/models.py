from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postCount = models.IntegerField(default=0)
    lovelyAuthors = models.ManyToManyField(User, through='UserLovelyAuthors', related_name='user_Author')



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
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор объявления')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.CharField(max_length=256, verbose_name='Содержание')
    status = models.CharField(max_length=6, choices=[('UNREAD', 'Непрочитанный'), ('READ', 'Прочитанный')], default='UNREAD',
                                verbose_name='Статус')

class UserLovelyAuthors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lovelyAuthors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='user_Author')