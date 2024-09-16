from django.db import models
from core.models.mixins import AbstractBase, AccountTransaction
from core.models.user import User


class PostOnlyAccount(AbstractBase):
    # Can only add transactions to this account
    users = models.ManyToManyField(User, related_name="post_only_accounts")


class PostOnlyTransaction(AccountTransaction):
    account = models.ForeignKey(
        PostOnlyAccount, on_delete=models.CASCADE, related_name="post_only_transactions"
    )

    class Meta:
        verbose_name = "Post Only Transaction"
        verbose_name_plural = "Post Only Transactions"
