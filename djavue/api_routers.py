from rest_framework import routers
from backend.api.viewsets import (
    UserView, ArticleGetPostView)

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'articles', ArticleGetPostView)