from rest_framework import serializers
from core.models import User
from core.serializers.abstract import AbstractSerializer


class UserSerializer(AbstractSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]
        read_only_field = ["is_active", "id"]

    def get_role(self, obj: User):
        return User.ROLE_CHOICES_MAP.get(obj.role)
