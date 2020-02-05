from django.contrib.auth.models import User
from rest_framework import serializers
import sys, os
sys.path.append('../')
from article.models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = Article
        fields = [
            'article_author',
            'article_title',
            'article_content',
            'date_posted',
        ]
