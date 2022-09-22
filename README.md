# WBTech_Blog (Веб-сервис + API)
Version: 0.1.0

## Выполненный функционал

1.Регистрироваться новым пользователям и выполнять вход существующих.
2.Авторизованным пользователям создавать посты. Пост имеет заголовок и текст поста.
3.Просматривать список пользователей с возможностью сортировки по количеству постов.
4.Просматривать список постов других пользователей, отсортированный по дате создания, сначала свежие.
5.Авторизованным пользователям подписываться и отписываться на посты других пользователей.
6.Авторизованным пользователям формировать ленту из постов пользователей, на которые была осуществлена подписка. В ленту попадают новые посты пользователей после выполнения подписки. Сортировка по дате создания поста, сначала свежие. Список постов отдается страницами по 10шт.
7.Авторизованным пользователям помечать посты в ленте как прочитанные.
8.Администратору управлять пользователями и контентом средствами Django admin.

## API (DjangoRestFramework)

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorListAPI* | [**api/v.0.1/list_create**](docs/SubmitDataApi.md#') | **GET**, **POST** /authors | Список авторов и добавление нового автора
*AuthorDetailAPI* | [**api/v.0.1/retrieve_partial_update_destroy**](docs/SubmitDataApi.md#) | **GET**,**PATCH**, **DELETE** /author/{id}/ |  Извлечение, редактирование и удаление автора
*PostListAPI* | [**api/v.0.1/list_create**](docs/SubmitDataApi.md#) | **GET** **POST** /posts | Список постов и добавление нового поста
*PostDetailAPI* | [**retrieve_partial_update_destroy**](docs/SubmitDataApi.md#api/v.0.1/) | **GET**,**PATCH**, **DELETE** /post/{id}/ | Извлечение, редактирование и удаление автора

