from rest_framework import serializers
from core.models import AllPermTransaction, PostOnlyTransaction, ViewOnlyTransaction
from core.serializers.abstract import AbstractSerializer


class BaseTransactionSerializer(AbstractSerializer):
    class Meta:
        fields = ["id", "amount", "date", "type", "created_at", "updated_at"]


class AllPermTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta):
        model = AllPermTransaction
        read_only_fields = ["id", "created_at", "updated_at"]


class PostOnlyTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta):
        model = PostOnlyTransaction
        read_only_fields = ["id", "created_at", "updated_at"]


class ViewOnlyTransactionSerializer(BaseTransactionSerializer):
    class Meta(BaseTransactionSerializer.Meta):
        model = ViewOnlyTransaction
        read_only_fields = ["id", "created_at", "updated_at"]
