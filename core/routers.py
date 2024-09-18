from rest_framework import routers
from core.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    ViewOnlyTransactionViewSet,
    PostOnlyTransactionViewSet,
    AllPermTransactionViewSet,
    AdminQueryTransactionViewSet,
)

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="register")
router.register(r"auth/login", LoginViewSet, basename="login")
router.register(r"auth/refresh", RefreshViewSet, basename="refresh")
router.register(
    r"transaction/view-only", ViewOnlyTransactionViewSet, basename="view-only"
)
router.register(
    r"transaction/post-only", PostOnlyTransactionViewSet, basename="post-only"
)
router.register(r"transaction/all-perm", AllPermTransactionViewSet, basename="all-perm")
router.register(
    r"transaction/admin-query", AdminQueryTransactionViewSet, basename="admin-query"
)

urlpatterns = [*router.urls]
