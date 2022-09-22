from django.test import TestCase
from models import *
# Create your tests here.

class PostCreateTest(TestCase):
    def setUp(self):
        new_user = User.objects.create_user(username='John Doe', password='?123456789pk!')
        new_author = Author.objects.create(user=new_user)
        new_post = Post.objects.create(author=new_author,
                                       title='Интересный заголовок',
                                       content='Вдохновляющий текст')

