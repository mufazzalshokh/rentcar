from modeltranslation.translator import register, TranslationOptions

from blog.models import PostModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
