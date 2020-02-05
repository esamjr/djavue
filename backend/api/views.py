from .serializers import ArticleSerializer
from rest_framework import viewsets
import sys
sys.path.append('../')
from article.models import Article

class ArticleViewSet(viewsets.ModelViewSet) :
    """
    API endpoint that allows article to be viewen or edited
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
