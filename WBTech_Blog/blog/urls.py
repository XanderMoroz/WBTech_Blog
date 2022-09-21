from django.urls import path
# Импортируем созданное нами представление
from .views import *

urlpatterns = [
    # авторы
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    # публикации
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    # публикации (CRUD)
    path('posts/create', PostCreate.as_view(), name='post_create'),
    path('posts/edit/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
    # подписка на авторов
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    # лента пользователя
    path('account/', UserPersonalPost.as_view(), name='user_account'),


    # Rest API (Авторы)
    path('api/v.0.1/authors', AuthorListAPI.as_view({'get': 'list', 'post': 'create'})),
    path('api/v.0.1/author/<int:pk>', AuthorDetailAPI.as_view({'get': 'retrieve',
                                                               'patch': 'partial_update',
                                                               'delete': 'destroy'})),
    # Rest API (Публикации)
    path('api/v.0.1/posts', PostListAPI.as_view({'get': 'list', 'post': 'create'})),
    path('api/v.0.1/post/<int:pk>', PostDetailAPI.as_view({'get': 'retrieve',
                                                           'patch': 'partial_update',
                                                           'delete': 'destroy'})),

    ]