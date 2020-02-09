from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path(r'admin/', admin.site.urls),

    # Api
    re_path(r'^api/v1/', include('djavue.routers')),
]
