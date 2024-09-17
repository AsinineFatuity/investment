from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from core.permissions import IsUserAdmin
from core.serializers import (
    AllPermTransactionSerializer,
    PostOnlyTransactionSerializer,
    ViewOnlyTransactionSerializer,
)
from core.models import AllPermTransaction, PostOnlyTransaction, ViewOnlyTransaction


class AdminQueryTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsUserAdmin]
    http_method_names = ["get"]
    authentication_classes = [JWTAuthentication]

    def list(self, request: HttpRequest, user_id=None):
        all_perm_transactions = AllPermTransaction.objects.filter(user_id=user_id)
        post_only_transactions = PostOnlyTransaction.objects.filter(user_id=user_id)
        view_only_transactions = ViewOnlyTransaction.objects.filter(user_id=user_id)
        all_perm_serializer = AllPermTransactionSerializer(
            all_perm_transactions, many=True
        )
        post_only_serializer = PostOnlyTransactionSerializer(
            post_only_transactions, many=True
        )
        view_only_serializer = ViewOnlyTransactionSerializer(
            view_only_transactions, many=True
        )
        return Response(
            {
                "all_perm_transactions": all_perm_serializer.data,
                "post_only_transactions": post_only_serializer.data,
                "view_only_transactions": view_only_serializer.data,
            },
            status=status.HTTP_200_OK,
        )
