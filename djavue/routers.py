from django.urls import path
import sys
sys.path.append('../backend/')
from api.viewsets import (
    ArticleView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView, 
    UserView)

article='articles'
user='users'
urlpatterns = [
    # Get response
    path('articles/', ArticleView.as_view()),
    path('users/', UserView.as_view()),
    
    # Create
    path('articles/create/', ArticleCreateView.as_view()),
    
    # Update
    path('articles/<int:pk>', ArticleUpdateView.as_view()),
    
    # Delete
    path('articles/delete/<int:pk>', ArticleDeleteView.as_view()),
]
