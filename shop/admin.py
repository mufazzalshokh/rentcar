from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from shop.forms import ColorModelForm
from shop.models import CategoryModel, BrandModel, CarModel, CarTagModel, ColorModel, CarImageModel


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
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


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['code']
    form = ColorModelForm


class CarImageStackedInline(admin.StackedInline):
    model = CarImageModel


@admin.register(CarModel)
class CarModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand', 'colors']
    readonly_fields = ['real_price']
    inlines = [CarImageStackedInline]
