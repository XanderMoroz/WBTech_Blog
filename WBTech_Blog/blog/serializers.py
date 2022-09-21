from rest_framework import serializers

from .models import Author, Post, User

class AuthorSerializer(serializers.ModelSerializer):
    """Сериализатор авторов"""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
       model = Author
       depth = 1
       fields = ['user', 'subscribers']

class PostSerializer(serializers.ModelSerializer):

    """Сериализатор координат перевала"""
    class Meta:
       model = Post
       depth = 1
       fields = ['author', 'title', 'content']
