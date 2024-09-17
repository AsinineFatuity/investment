from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.permissions import PermChecker, HasAllTransactionPerm
from core.serializers import AllPermTransactionSerializer
from core.models import AllPermAccount, AllPermTransaction


class AllPermTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated, HasAllTransactionPerm]
    http_method_names = ["get", "post", "delete", "put"]
    authentication_classes = []

    def list(self, request: HttpRequest):
        user_transactions = AllPermTransaction.objects.filter(user_id=request.user.id)
        serializer = AllPermTransactionSerializer(user_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request: HttpRequest, pk=None):
        transaction = AllPermTransaction.objects.get(public_id=pk)
        serializer = AllPermTransactionSerializer(transaction, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: HttpRequest):
        serializer = AllPermTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account_id = AllPermAccount.objects.first().id
        serializer.save(account_id=account_id, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
