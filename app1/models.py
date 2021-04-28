from django.db import models
from django_currentuser.db.models import CurrentUserField


class Article(models.Model):
    title = models.CharField(max_length=120, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(null=True, upload_to='static')
    user_id = CurrentUserField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=False, null=False)
    article_id = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    user_id = CurrentUserField()
