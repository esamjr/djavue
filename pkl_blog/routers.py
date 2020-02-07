import sys
from rest_framework import routers
sys.path.append('../backend/')
from api.viewsets import (
    UserViewSet, ArticleViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)
