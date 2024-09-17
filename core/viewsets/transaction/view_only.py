from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.permissions import PermChecker
from core.serializers import ViewOnlyTransactionSerializer
from core.models import ViewOnlyTransaction


class ViewOnlyTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]
    authentication_classes = []

    def list(self, request: HttpRequest):
        user_transactions = ViewOnlyTransaction.objects.filter(user=request.user)
        serializer = ViewOnlyTransactionSerializer(user_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: HttpRequest):
        perm_checker = PermChecker(request.user)
        user_has_perm = perm_checker.user_has_perm(
            PermChecker.ADD_ACTION, PermChecker.VIEW_ONLY_TRANSACTION_MODEL
        )
        if not user_has_perm:
            return Response(
                {"detail": "You do not have permission to perform this action"},
                status=status.HTTP_403_FORBIDDEN,
            )
