from rest_framework import routers
from django.urls import re_path
from core.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
    ViewOnlyTransactionViewSet,
    PostOnlyTransactionViewSet,
    AllPermTransactionViewSet,
    AdminQueryTransactionView,
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

urlpatterns = [*router.urls]
urlpatterns.append(
    re_path(
        r"^transaction/admin-query/(?P<user_id>[^/]+)(/(?P<start_date>[^/]+))?(/(?P<end_date>[^/]+))?/$",
        AdminQueryTransactionView.as_view(),
        name="admin-query",
    ),
)
