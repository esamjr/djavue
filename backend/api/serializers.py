from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('../')
from article.models import Article

class UserSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = User
        fields = [
            'id',
            'username',
            'password',
            'email'
        ]
class ArticleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = Article
        fields = [
            'author',
            'title',
            'content',
            'date_posted',
        ]
