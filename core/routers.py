from rest_framework import routers
from core.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    ViewOnlyTransactionViewSet,
)

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="register")
router.register(r"auth/login", LoginViewSet, basename="login")
router.register(r"auth/refresh", RefreshViewSet, basename="refresh")
router.register(
    r"transaction/view-only", ViewOnlyTransactionViewSet, basename="view-only"
)
urlpatterns = [*router.urls]
