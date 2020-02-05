from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('../')
from article.models import Article

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = User
        fields = [
            'url',
            'username',
        ]

class ArticleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = Article
        fields = [
            'article_author',
            'article_title',
            'article_content',
            'date_posted',
        ]
