from django.contrib.auth.models import User
from rest_framework import serializers
import sys
sys.path.append('../')
from article.models import article

class ArticleSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model  = article
        fields = [
            'author',
            'title',
            'content',
            'date_posted',
        ]
