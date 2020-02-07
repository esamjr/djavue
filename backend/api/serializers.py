from article.models import Article
from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('../')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'date_joined',
        ]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'user',
            'title',
            'content',
            'date_posted',
        ]
