from django.contrib.auth.models import User
from django.utils.timezone import now
from rest_framework import serializers
from article.models import Article
import datetime
import sys
sys.path.append('../')

class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=30)
    email=serializers.EmailField(max_length=30)
    
    def create(self, validated_data) :
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data) :
        instance.user=validated_data.get('username',instance.username)
        instance.title=validated_data.get('email',instance.email)
        
        instance.save()
        return instance

class ArticleSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField(required=False)
    user=serializers.CharField(max_length=60)
    title=serializers.CharField(max_length=60)
    content=serializers.CharField(max_length=2000)
    date_posted=serializers.DateField(default=datetime.date.today)
    
    def create(self, validated_data) :
        return Article.objects.create(**validated_data)

    def update(self,instance,validated_data) :
        instance.id=validated_data.get('id',instance.id)
        instance.user=validated_data.get('user',instance.user)
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.date_posted=validated_data.get('date_posted',instance.date_posted)
        
        instance.save()
        return instance
