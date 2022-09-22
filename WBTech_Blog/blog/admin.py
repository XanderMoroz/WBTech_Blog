from django.contrib import admin
from .models import Post, Author, UserSubscribers, UserReadPost

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(UserSubscribers)
admin.site.register(UserReadPost)