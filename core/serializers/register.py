from rest_framework import serializers
from core.serializers.user import UserSerializer


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, required=True, write_only=True
    )

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ["password"]
