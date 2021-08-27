from django.contrib import admin

from shop.models import CategoryModel, BrandModel, CarModel, CarTagModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CarTagModel)
class CarTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand']
