from typing import Dict, Any
from datetime import datetime, timedelta
from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase
from core.models import (
    PostOnlyTransaction,
    AllPermTransaction,
    PostOnlyAccount,
    AllPermAccount,
)
from core.models.mixins import TransactionTypeEnum
from core.models.user import RolesEnum


class TestAdminQueryTransactions(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.admin_query_transaction_url = reverse(
            "admin-query-fetch-transactions", args=[str(self.user.public_id)]
        )
        self.post_only_account = PostOnlyAccount.objects.first()
        self.all_perm_account = AllPermAccount.objects.first()
        self.transaction_date = "2024-09-01"
        self.withdrawal_amount = 200
        self.deposit_amount = 1000
        self.expected_account_balance = self.deposit_amount - self.withdrawal_amount
        self.create_transaction_data()

    def create_transaction_data(self):
        withdrawal_data = {
            "amount": self.withdrawal_amount,
            "type": TransactionTypeEnum.W,
            "user": self.user,
            "date": self.transaction_date,
        }
        deposit_data = {
            "amount": self.deposit_amount,
            "type": TransactionTypeEnum.D,
            "user": self.user,
            "date": self.transaction_date,
        }
        all_account_data = [withdrawal_data, deposit_data]
        post_to_create = []
        all_to_create = []
        for data in all_account_data:
            post_to_create.append(
                PostOnlyTransaction(account=self.post_only_account, **data)
            )
            all_to_create.append(
                AllPermTransaction(account=self.all_perm_account, **data)
            )
        post_only_transactions = PostOnlyTransaction.objects.bulk_create(post_to_create)
        all_perm_transactions = AllPermTransaction.objects.bulk_create(all_to_create)
        self.total_post_transactions = len(post_only_transactions)
        self.total_all_perm_transactions = len(all_perm_transactions)
        self.total_view_only_transactions = 0

    def test_non_admin_user_cannot_query_transactions(self):
        response = self.client.get(self.admin_query_transaction_url)
        self.assertEqual(
            str(response.data["detail"]),
            "You do not have permission to perform this action.",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def assertCorrectTransactionsDataReturned(
        self,
        all_perm_trans_data: Dict[str, Any],
        post_only_trans_data: Dict[str, Any],
        view_only_trans_data: Dict[str, Any],
    ):
        # assert all perm transaction data
        self.assertEqual(
            len(all_perm_trans_data["transactions"]), self.total_all_perm_transactions
        )
        self.assertEqual(
            all_perm_trans_data["account_balance"], self.expected_account_balance
        )
        # assert post only transaction data
        self.assertEqual(
            len(post_only_trans_data["transactions"]), self.total_post_transactions
        )
        self.assertEqual(
            post_only_trans_data["account_balance"], self.expected_account_balance
        )
        # assert view only transaction data
        self.assertEqual(
            len(view_only_trans_data["transactions"]), self.total_view_only_transactions
        )
        self.assertEqual(view_only_trans_data["account_balance"], 0)

    def test_get_admin_query_transaction_without_date_filter_expect_data(self):
        self.user.is_staff = True
        self.user.role = RolesEnum.ADMIN
        self.user.save()
        query_params = {"start_date": "", "end_date": ""}
        response = self.client.post(self.admin_query_transaction_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        all_perm_trans_data = data["all_perm_transactions"]
        post_only_trans_data = data["post_only_transactions"]
        view_only_trans_data = data["view_only_transactions"]
        self.assertCorrectTransactionsDataReturned(
            all_perm_trans_data, post_only_trans_data, view_only_trans_data
        )

    def test_get_admin_query_transaction_with_date_filter_expect_data(self):
        self.user.is_staff = True
        self.user.role = RolesEnum.ADMIN
        self.user.save()
        query_params = {
            "start_date": self.transaction_date,
            "end_date": self.transaction_date,
        }
        response = self.client.post(self.admin_query_transaction_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.data
        all_perm_trans_data = data["all_perm_transactions"]
        post_only_trans_data = data["post_only_transactions"]
        view_only_trans_data = data["view_only_transactions"]
        self.assertCorrectTransactionsDataReturned(
            all_perm_trans_data, post_only_trans_data, view_only_trans_data
        )

    def test_get_admin_query_transaction_with_date_filter_expect_no_data(self):
        self.user.is_staff = True
        self.user.role = RolesEnum.ADMIN
        self.user.save()
        date_format = "%Y-%m-%d"
        date_without_transactions = datetime.strptime(
            self.transaction_date, date_format
        ) + timedelta(days=1)
        query_date = date_without_transactions.strftime(date_format)
        query_params = {"start_date": query_date, "end_date": query_date}
        response = self.client.post(self.admin_query_transaction_url, query_params)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # assert that transactions actually exist
        self.assertGreater(self.total_post_transactions, 0)
        self.assertGreater(self.total_all_perm_transactions, 0)
        data = response.data
        # assert all perm transaction data
        all_perm_trans_data = data["all_perm_transactions"]
        self.assertEqual(len(all_perm_trans_data["transactions"]), 0)
        self.assertEqual(all_perm_trans_data["account_balance"], 0)
        # assert post only transaction data
        post_only_trans_data = data["post_only_transactions"]
        self.assertEqual(len(post_only_trans_data["transactions"]), 0)
        self.assertEqual(post_only_trans_data["account_balance"], 0)
        # assert view only transaction data
        view_only_trans_data = data["view_only_transactions"]
        self.assertEqual(len(view_only_trans_data["transactions"]), 0)
        self.assertEqual(view_only_trans_data["account_balance"], 0)
