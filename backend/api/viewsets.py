from .serializers import (
    ArticleSerializer, UserSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from article.models import Article


class UserView(APIView):
    """
    API Endpoint that allows users to be viewed or edited
    """
    def get(self, request) :
        queryset = User.objects.all().order_by('-date_joined')
        
        serializer = UserSerializer(queryset, many = True)
        return Response({'users': serializer.data})

# CREATE
class ArticleView(APIView):
    """
    API endpoint that allows article to be viewed
    """
    def get(self, request) :
        queryset = Article.objects.all()
        serializer = ArticleSerializer(queryset, many = True)
        return Response({'articles': serializer.data})

# Create
class ArticleCreateView(APIView) :
    """
    API endpoint that allows article to be created
    """
    def post(self, request) :
        articles = request.data.get('article')
        
        # Create new Article based data above
        serializer = ArticleSerializer(data = articles)
        if serializer.is_valid(raise_exception = True) :
            article_saved = serializer.save()
            
        return Response({"success": "Article {} created successfully".format(article_saved.title)})

# Update | PUT
class ArticleUpdateView(APIView) :
    """
    API endpoint that allows article to be viewed or edited
    """
    def get(self, request, pk) :
        if not get_object_or_404(Article.objects.filter(id=pk)) :
            return False
        
        queryset = Article.objects.filter(id=pk)
        serializer = ArticleSerializer(queryset, many = True)
        return Response({'articles': serializer.data})
    
    def put(self, request, pk) :
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        
        # [partial = True]
        # passing partial=True to the serializer since we want to be able to 
        # update some fields but not necessarily all at once. 
        serializer = ArticleSerializer(
            instance = saved_article, data = data, partial = True
        )
        if serializer.is_valid(raise_exception = True) :
            article_saved = serializer.save()

        return Response({"success":"Article '{}' updated successfully".format(article_saved.title)})

# DELETE | DELETE
class ArticleDeleteView(APIView) :
    """
    API endpoint that allows article to be viewed or deleted
    """
    def get(self, request, pk) :
        if not get_object_or_404(Article.objects.filter(id=pk)) :
            return False
        
        queryset = Article.objects.filter(id=pk)
        serializer = ArticleSerializer(queryset, many = True)
        return Response({'articles': serializer.data})
    
    def delete(self, request, pk) :
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article_title = article.title
        article.delete()
        
        return Response({"success":"Article with title '{}' has been deleted".format(article_title)}, status = 204)