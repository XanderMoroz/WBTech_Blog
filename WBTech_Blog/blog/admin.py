from django.contrib import admin
from .models import Post, Author, UserLovelyAuthors

# Register your models here.
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(UserLovelyAuthors)