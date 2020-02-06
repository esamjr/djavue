from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from article.models import Article

class UserViewSet(viewsets.ModelViewSet) :
    """
    API Endpoint that allows user to be viewen or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet) :
    """
    API endpoint that allows article to be viewen or edited
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
