from django.urls import path
# Импортируем созданное нами представление
from .views import AuthorList, AuthorDetail


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),


    ]