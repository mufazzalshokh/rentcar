from django.contrib import admin

from blog.models import PostTagModel, PostModel, CommentModel


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'price', 'created_at']
    list_filter = ['tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['tags']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
