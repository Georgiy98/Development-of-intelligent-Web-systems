from django.urls import path
from .views import get_all_articles, get_article, get_all_users, get_user_articles

urlpatterns = [
    path('articles', get_all_articles, name='article_list'),
    path('article/<int:article_id>', get_article, name='article_form'),
    path('users/', get_all_users, name='user_list'),
    path('user_articles/<int:user_id>', get_user_articles, name='user_articles')
]
