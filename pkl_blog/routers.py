import sys
from rest_framework import routers
sys.path.append('../backend/')
from api import viewsets

router = routers.DefaultRouter()
router.register('users', viewsets.UserViewSet)
router.register('profile', viewsets.ProfileViewSet)
router.register('article', viewsets.ArticleViewSet)
