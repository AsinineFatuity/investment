from core.models import User
from core.serializers.abstract import AbstractSerializer
from core.permissions import CreatePermission


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_field = ["is_active", "id"]

    def create(self, validated_data):
        user = super().create(validated_data)
        CreatePermission(user).add_user_to_groups()
        return super().create(validated_data)
