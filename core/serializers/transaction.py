from rest_framework import serializers
from core.models import AllPermTransaction, PostOnlyTransaction, ViewOnlyTransaction


class AllPermTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllPermTransaction
        read_only_fields = ["id", "created_at", "updated_at"]


class PostOnlyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOnlyTransaction
        read_only_fields = ["id", "created_at", "updated_at"]


class ViewOnlyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewOnlyTransaction
        read_only_fields = ["id", "created_at", "updated_at"]
