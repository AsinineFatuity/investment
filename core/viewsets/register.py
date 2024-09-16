from django.http import HttpRequest
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from core.serializers import RegisterSerializer
from core.permissions import CreatePermission


class RegisterViewSet(ViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    http_method_names = ["post"]
    authentication_classes = []

    @transaction.atomic
    def create(self, request: HttpRequest):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        CreatePermission(user).add_user_to_groups()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
