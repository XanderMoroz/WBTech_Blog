from django.contrib import admin
from .models import Post, Author, UserSubscribers

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(UserSubscribers)