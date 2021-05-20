from django.contrib import admin
from .models import Article, Comment
from modeltranslation.admin import TranslationAdmin


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'user_id')


@admin.register(Comment)
class CommentAdmin(TranslationAdmin):
    list_display = ('article_id', 'user_id')
