from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleSerializer, UserSerializer

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
    
@api_view(['GET','PUT', 'DELETE'])
def update_delete(request, pk) : 
    """
    API Endpoint that allows users to be edited or deleted
    """
    if request.method == "GET" :
        set_queryset   = Article.objects.filter(id = pk)
        set_serializer = ArticleSerializer(set_queryset, many = True)
        return Response({'articles': set_serializer.data})

    if request.method == "PUT" :
        the_article = get_object_or_404(Article.objects.all(), pk = pk)
        data        = request.data.get('article')
        serializer  = ArticleSerializer(
            the_article, data = data, partial = True)
        
        if serializer.is_valid(raise_exception = True) :
            serializer.save()
            return Response({"success":"Article successfully updated"})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE" :
        articles  = get_object_or_404(Article.objects.all(), pk = pk)
        operation = articles.delete()
        if operation :
            return Response({"success":"Article successfully deleted"})
        else :
            return Response({"failed":"Failed to delete"})

@api_view(['GET', 'POST'])
def get_post(request) :
    """
    API Endpoint that allows users to be viewed or created
    """
    if request.method == "GET" :
        queryset   = Article.objects.all()
        serializer = ArticleSerializer(queryset, many = True)
        return Response(serializer.data)
    
    if request.method == "POST" :
        articles   = request.data.get('article') 
        serializer = ArticleSerializer(data = articles)
        if serializer.is_valid(raise_exception = True) :
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    