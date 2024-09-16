from rest_framework import serializers
from core.serializers.user import UserSerializer
from core.permissions import CreatePermission


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, required=True, write_only=True
    )

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ["password"]

    def create(self, validated_data):
        user = super().create(validated_data)
        CreatePermission(user).add_user_to_groups()
        return super().create(validated_data)
