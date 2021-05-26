from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext_lazy as _


class Article(models.Model):
    title = models.CharField(max_length=120, null=False, verbose_name=_('title'))
    content = models.TextField(null=False, verbose_name=_('content'))
    image = models.ImageField(null=True, upload_to='static', verbose_name=_('image'))
    user_id = CurrentUserField(verbose_name=_('author'))
    similar_article_ids = models.ManyToManyField('self', blank=True, verbose_name=_('similar articles'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')


class Comment(models.Model):
    text = models.TextField(blank=False, null=False, verbose_name=_('text'))
    article_id = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE,
                                   verbose_name=_('article'))
    user_id = CurrentUserField(verbose_name=_('author'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
