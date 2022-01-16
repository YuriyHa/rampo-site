from django.contrib import admin

from news.views import post
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
# Register your models here.
