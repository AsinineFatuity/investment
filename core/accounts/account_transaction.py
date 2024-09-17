from typing import Union
from datetime import datetime
from core.models import User, AllPermTransaction, PostOnlyTransaction


class AccountTransaction:
    def __init__(
        self,
        user: User,
        account_id: int,
        transaction_cls: Union[AllPermTransaction, PostOnlyTransaction],
        amount: float,
        date: Union[datetime.date, str],
        transaction_type: str,
        transaction_obj: Union[AllPermTransaction, PostOnlyTransaction] = None,
    ):
        self._transaction_cls = transaction_cls
        self._user = user
        self._account_id = account_id
        self._amount = amount
        self._date = date
        self._transaction_type = transaction_type
        self._transaction_obj = transaction_obj

    def create_transaction(self):
        transaction = self._transaction_cls.objects.create(
            account_id=self._account_id,
            user=self._user,
            amount=self._amount,
            date=self._date,
            type=self._transaction_type,
        )
        return transaction

    def update_transaction(self):
        self._transaction_obj.amount = self._amount
        self._transaction_obj.date = self._date
        self._transaction_obj.type = self._transaction_type
        self._transaction_obj.save()
        return self._transaction_obj

    def delete_transaction(self):
        self._transaction_obj.delete()
        return True
