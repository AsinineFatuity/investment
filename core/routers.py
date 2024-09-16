from rest_framework import routers
from core.viewsets.register import RegisterViewSet
from core.viewsets.login import LoginViewSet

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="register")
router.register(r"auth/login", LoginViewSet, basename="login")
urlpatterns = [*router.urls]
