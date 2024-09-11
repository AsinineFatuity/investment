from django.db import models
from core.models.mixins import AbstractBase
from core.models.user import User


class ViewOnlyAccount(AbstractBase):
    users = models.ManyToManyField(User, related_name="view_only_accounts")
