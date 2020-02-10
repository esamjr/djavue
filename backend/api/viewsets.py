from django.shortcuts import get_object_or_404, redirect
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
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer

    def put(self, request, pk):
        saved_article  = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})



    @api_view(['DELETE'])
    def delete(self, request, pk) :
        article = get_object_or_404(Article.objects.all(), pk = pk)
        article.delete()
        return Response(status = status.HTTPS_200_OK)