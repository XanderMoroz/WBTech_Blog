from django.urls import path
# Импортируем созданное нами представление
from .views import *

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),

    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    ]