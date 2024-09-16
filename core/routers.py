from rest_framework import routers
from core.viewsets.register import RegisterViewSet

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="register")
urlpatterns = [*router.urls]
