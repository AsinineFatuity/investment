from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.permissions import CheckPermission
from core.serializers import ViewOnlyTransactionSerializer
from core.models import ViewOnlyTransaction


class ViewOnlyTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]

    def list(self, request: HttpRequest):
        user_transactions = ViewOnlyTransaction.objects.filter(user=request.user)
        serializer = ViewOnlyTransactionSerializer(user_transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
