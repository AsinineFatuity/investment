from rest_framework import serializers
from core.models import User
from core.serializers.abstract import AbstractSerializer


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
