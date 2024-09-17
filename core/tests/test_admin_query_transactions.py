from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase
from core.models import (
    PostOnlyTransaction,
    AllPermTransaction,
    PostOnlyAccount,
    ViewOnlyAccount,
    AllPermAccount,
)
from core.models.mixins import TransactionTypeEnum
from core.models.user import RolesEnum
from django.test import tag


class TestAdminQueryTransactions(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.admin_query_transaction_url = reverse("admin-query-list")
        self.post_only_account = PostOnlyAccount.objects.first()
        self.all_perm_account = AllPermAccount.objects.first()
        self.create_transaction_data()

    def create_transaction_data(self):
        withdrawal_data = {
            "amount": 200,
            "type": TransactionTypeEnum.W,
            "user": self.user,
            "date": "2024-09-01",
        }
        deposit_data = {
            "amount": 1000,
            "type": TransactionTypeEnum.D,
            "user": self.user,
            "date": "2024-09-01",
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
        PostOnlyTransaction.objects.bulk_create(post_to_create)
        AllPermTransaction.objects.bulk_create(all_to_create)

    def test_non_admin_user_cannot_query_transactions(self):
        response = self.client.get(self.admin_query_transaction_url)
        self.assertEqual(
            str(response.data["detail"]),
            "You do not have permission to perform this action.",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @tag("rel")
    def test_get_admin_query_transaction(self):
        self.user.is_staff = True
        self.user.role = RolesEnum.ADMIN
        self.user.save()
        query_params = {
            "user_id": self.user.id,
        }
        response = self.client.get(
            reverse("admin-query-list"), {"user_id": self.user.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
