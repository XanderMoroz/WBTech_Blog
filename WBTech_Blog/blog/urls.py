from django.urls import path
# Импортируем созданное нами представление
from .views import *

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),

    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('posts/create', PostCreate.as_view(), name='post_create'),
    path('posts/edit/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),

    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    ]