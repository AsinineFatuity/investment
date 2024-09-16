from rest_framework import routers
from core.viewsets import RegisterViewSet, LoginViewSet, RefreshViewSet

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="register")
router.register(r"auth/login", LoginViewSet, basename="login")
router.register(r"auth/refresh", RefreshViewSet, basename="refresh")
urlpatterns = [*router.urls]
