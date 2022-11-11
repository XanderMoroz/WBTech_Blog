### WBTech_Blog (Веб-сервис + API)
Version: 0.1.0 
![Screen Shot](Demo_scrincast.gif)

### Описание проекта

WBTech_Blog представляет собой сервис авторских блогов. Благодаря своим функциям сервис выступает в качестве площадки взаимодействия - общения и обмена информацией.

#### Возможности сервиса:

1. Регистрироваться новым пользователям и выполнять вход существующих.
2. Авторизованным пользователям создавать посты. Пост имеет заголовок и текст поста.
3. Просматривать список пользователей с возможностью сортировки по количеству постов.
4. Просматривать список постов других пользователей, отсортированный по дате создания, сначала свежие.
5. Авторизованным пользователям подписываться и отписываться на посты других пользователей.
6. Авторизованным пользователям формировать ленту из постов пользователей, на которые была осуществлена подписка. В ленту попадают новые посты пользователей после выполнения подписки. Сортировка по дате создания поста, сначала свежие. Список постов отдается страницами по 10шт.
7. Авторизованным пользователям помечать посты в ленте как прочитанные.
8. Администратору управлять пользователями и контентом средствами Django admin.

### Стек технологий 

В ходе создания проекта применялись различные инстументы и технологии. Они представлены ниже:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)

### API (DjangoRestFramework)

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorListAPI* | [**api/v.0.1/list_create**](docs/SubmitDataApi.md#') | **GET**, **POST** /authors | Список авторов и добавление нового автора
*AuthorDetailAPI* | [**api/v.0.1/retrieve_partial_update_destroy**](docs/SubmitDataApi.md#) | **GET**,**PATCH**, **DELETE** /author/{id}/ |  Извлечение, редактирование и удаление автора
*PostListAPI* | [**api/v.0.1/list_create**](docs/SubmitDataApi.md#) | **GET** **POST** /posts | Список постов и добавление нового поста
*PostDetailAPI* | [**retrieve_partial_update_destroy**](docs/SubmitDataApi.md#api/v.0.1/) | **GET**,**PATCH**, **DELETE** /post/{id}/ | Извлечение, редактирование и удаление поста


### Инструкция по установке 

1. Клонируете репозиторий

```sh
git clone https://github.com/XanderMoroz/WBTech_Blog.git
```
2. Уставливаете виртуальное окружение (virtual environment)
```sh
pip install virtualenv
```
3. Активируете виртуальное окружение
```sh
./venv/scripts/activate
```
4. Переходите в дерикторию проекта Наслаждаетесь результатом!
```sh
cd ./Fan-game_service-board/
```
5. Устанавливаете зависимости
```sh
pip install -r requirements.txt
```
6. Запускаете сервер
```sh
python manage.py runserver
```
7. Наслаждаетесь результатом)

### Лицензия

Лицензия не требуется. Проект может быль использован без ограничений. 

### Авторы

* [XanderMoroz](https://https://github.com/XanderMoroz/) - *Все работы*

