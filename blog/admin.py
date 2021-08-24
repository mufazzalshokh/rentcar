from django.contrib import admin

from blog.models import PostTagModel, PostModel


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['tags']
