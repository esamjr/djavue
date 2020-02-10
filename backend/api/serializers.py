from rest_framework import serializers
import datetime

from django.contrib.auth.models import User
from article.models import Article

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model  = User
        fields = [
            'id',
            'username',
            'email'
        ]

class ArticleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = Article
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'content',
            'date_posted'
        ]
