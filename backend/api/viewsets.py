from .serializers import ArticleSerializer, ProfileSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from article.models import Article
from users.models import Profile

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
