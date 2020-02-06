from .serializers import (
    ArticleSerializer, ProfileSerializer, UserSerializer)
from django.contrib.auth.models import User
from rest_framework import viewsets
from article.models import Article
from users.models import Profile

class UserViewSet(viewsets.ModelViewSet) :
    """
    API Endpoint that allows users to be viewen or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet) :
    """
    API Endpoint that allows profile to be viewen or edited
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ArticleViewSet(viewsets.ModelViewSet) :
    """
    API endpoint that allows article to be viewen or edited
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
