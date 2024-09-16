from django.contrib import admin
from django.urls import path
from core.routers import urlpatterns as api_routers

urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += api_routers
