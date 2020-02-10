from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework import status
from .serializers import ArticleSerializer, UserSerializer

from django.contrib.auth.models import User
from article.models import Article


class UserView(viewsets.ModelViewSet) :
    """
    API Endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ArticleGetPostView(viewsets.ModelViewSet) :
    """
    API Endpoint that allows articles to be viewed or edited
    """
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    
    def update(self, request, pk) :
        article    = get_object_or_404(Article.objects.all(), pk = pk)
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk) :
        article = get_object_or_404(Article.objects.all(), pk = pk)
        article.delete()
        return Response(status = status.HTTPS_200_OK)