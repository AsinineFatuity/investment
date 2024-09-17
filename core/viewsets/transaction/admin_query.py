from django.http import HttpRequest
from django.db.models import Sum, Case, When, Value, DecimalField
from django.db.models.functions import Coalesce
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from core.permissions import IsUserAdmin
from core.serializers import (
    AllPermTransactionSerializer,
    PostOnlyTransactionSerializer,
    ViewOnlyTransactionSerializer,
)
from core.models import AllPermTransaction, PostOnlyTransaction, ViewOnlyTransaction
from core.models.mixins import TransactionTypeEnum


class AdminQueryTransactionViewSet(ViewSet):
    permission_classes = [IsAuthenticated, IsUserAdmin]
    http_method_names = ["get"]
    authentication_classes = [JWTAuthentication]

    def list(
        self,
        request: HttpRequest,
        user_id=None,
        start_date=None,
        end_date=None,
        **kwargs
    ):
        print(kwargs)
        print("user_id", user_id)
        # get transactions for a specific user
        all_perm_transactions = AllPermTransaction.objects.all()
        post_only_transactions = PostOnlyTransaction.objects.all()
        view_only_transactions = ViewOnlyTransaction.objects.all()
        if start_date:
            all_perm_transactions = all_perm_transactions.filter(date__gte=start_date)
            post_only_transactions = post_only_transactions.filter(date__gte=start_date)
            view_only_transactions = view_only_transactions.filter(date__gte=start_date)
        if end_date:
            all_perm_transactions = all_perm_transactions.filter(date__lte=end_date)
            post_only_transactions = post_only_transactions.filter(date__lte=end_date)
            view_only_transactions = view_only_transactions.filter(date__lte=end_date)
        # calculate balances for each account type
        balances_transactions_map = {
            "all_perm_balance": all_perm_transactions,
            "post_only_balance": post_only_transactions,
            "view_only_balance": view_only_transactions,
        }
        account_balances_map = {
            "all_perm_balance": 0,
            "post_only_balance": 0,
            "view_only_balance": 0,
        }
        for account_type, transactions in balances_transactions_map.items():
            balances_transactions_map[account_type] = transactions.aggregate(
                all_deposits=Coalesce(
                    Sum(Case(When(type=TransactionTypeEnum.D, then="amount"))),
                    Value(0),
                    output_field=DecimalField(),
                ),
                all_withdrawals=Coalesce(
                    Sum(Case(When(type=TransactionTypeEnum.W, then="amount"))),
                    Value(0),
                    output_field=DecimalField(),
                ),
            )
            account_balances_map[account_type] = (
                balances_transactions_map[account_type]["all_deposits"]
                - balances_transactions_map[account_type]["all_withdrawals"]
            )

        all_perm_serializer = AllPermTransactionSerializer(
            all_perm_transactions, many=True
        )
        post_only_serializer = PostOnlyTransactionSerializer(
            post_only_transactions, many=True
        )
        view_only_serializer = ViewOnlyTransactionSerializer(
            view_only_transactions, many=True
        )
        return Response(
            {
                **account_balances_map,
                "all_perm_transactions": all_perm_serializer.data,
                "post_only_transactions": post_only_serializer.data,
                "view_only_transactions": view_only_serializer.data,
            },
            status=status.HTTP_200_OK,
        )
