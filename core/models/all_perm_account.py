from django.db import models
from core.models.mixins import AbstractBase
from core.models.user import User


class AllPermAccount(AbstractBase):
    users = models.ManyToManyField(User, related_name="all_perm_accounts")
