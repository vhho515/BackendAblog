from django.contrib import admin
from .models import Post


class PostList(admin.ModelAdmin):
    list_display = ('title', 'name', 'body', 'year')
    list_filter = ('title', 'name', 'year',)
    search_fields = ('title', 'name', 'body', 'year')
    ordering = ['year']


admin.site.register(Post, PostList)
