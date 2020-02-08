from django.urls import path
from backend.api.viewsets import get_post, update_delete

article = 'articles'
user    = 'users'

urlpatterns = [
    # Get response
    path('articles/', get_post),
    path('articles/<int:pk>', update_delete),
]
