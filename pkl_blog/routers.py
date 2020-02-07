from api.viewsets import (
    UserViewSet, ArticleViewSet)
import sys
from rest_framework import routers
sys.path.append('../backend/')

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)
