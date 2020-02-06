from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('../')
from article.models import Article
from users.models import Profile

class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = User
        fields = [
            'id',
            'email',
            'username',
            'date_joined',
        ]

class ProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Profile
        fields = [
            'id',
            'username',
        ]

class ArticleSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Article
        fields = [
            'id',
            'user',
            'title',
            'content',
            'date_posted',
        ]
