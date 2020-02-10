from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from djavue.api_routers import router


urlpatterns = [
    path(r'admin/', admin.site.urls),

    # Api
    re_path('api/v1/', include(router.urls)),
]
