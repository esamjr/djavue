import sys
from rest_framework import routers
sys.path.append('../backend/')
from api import viewsets

router = routers.DefaultRouter()
router.register('article', viewsets.ArticleViewSet)
router.register('profile', viewsets.ProfileViewSet)
