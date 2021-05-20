from modeltranslation.translator import register, TranslationOptions
from .models import Article, Comment


@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Comment)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('text',)
