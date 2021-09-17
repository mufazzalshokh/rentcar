from modeltranslation.translator import register, TranslationOptions

from shop.models import CategoryModel, CarModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CarModel)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
