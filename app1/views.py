from django.shortcuts import render
from .models import Article
from django.contrib.auth.models import User
from django.utils.translation import gettext


def get_all_articles(request):
    text = render(request, 'article_list.html', context={
        'title': 'Articles',
        'article_list': Article.objects.all()
    })
    return render(request, 'article_list.html', context={
        'title': 'Articles',
        'article_list': Article.objects.all()
    })


def get_all_users(request):
    return render(request, 'user_list.html', context={
        'user_list': User.objects.all()
    })


def get_user_articles(request, user_id):
    return render(request, 'article_list.html', context={
        'title': User.objects.get(pk=user_id).get_full_name(),
        'article_list': Article.objects.filter(user_id=user_id)
    })


def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'article_form.html', context={
        'title': article.title,
        'image_url': article.image.url,
        'content': article.content,
        'comment_list': article.comment_set.all(),
        'similar_articles': article.similar_article_ids.all(),
    })
