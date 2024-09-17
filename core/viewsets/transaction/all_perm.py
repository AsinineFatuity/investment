from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from core.permissions import PermChecker
from core.serializers import AllPermTransactionSerializer
from core.models import PostOnlyAccount


class AllPermTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post"]
    authentication_classes = []

    def list(self, request: HttpRequest):
        perm_checker = PermChecker(request.user)
        user_has_perm = perm_checker.user_has_perm(
            PermChecker.VIEW_ACTION, PermChecker.POST_ONLY_TRANSACTION_MODEL
        )
        if not user_has_perm:
            return Response(
                {"detail": "You do not have permission to perform this action"},
                status=status.HTTP_403_FORBIDDEN,
            )

    def create(self, request: HttpRequest):
        serializer = AllPermTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account_id = PostOnlyAccount.objects.first().id
        serializer.save(account_id=account_id, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
