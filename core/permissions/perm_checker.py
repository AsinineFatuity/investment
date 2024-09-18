from rest_framework.permissions import BasePermission
from django.http import HttpRequest
from core.models import (
    ViewOnlyTransaction,
    PostOnlyTransaction,
    AllPermTransaction,
)
from core.models.user import User, RolesEnum


class PermChecker:
    # Define possible actions
    VIEW_ACTION = "view"
    ADD_ACTION = "add"
    CHANGE_ACTION = "change"
    DELETE_ACTION = "delete"
    VALID_ACTIONS = [VIEW_ACTION, ADD_ACTION, CHANGE_ACTION, DELETE_ACTION]
    # valid model names
    VIEW_ONLY_TRANSACTION_MODEL = ViewOnlyTransaction.__name__.lower()
    POST_ONLY_TRANSACTION_MODEL = PostOnlyTransaction.__name__.lower()
    ALL_PERM_TRANSACTION_MODEL = AllPermTransaction.__name__.lower()
    VALID_MODELS = [
        VIEW_ONLY_TRANSACTION_MODEL,
        POST_ONLY_TRANSACTION_MODEL,
        ALL_PERM_TRANSACTION_MODEL,
    ]

    def __init__(self, user: User):
        self._user = user

    def user_has_perm(self, action: str, model_name: str):
        if action not in self.VALID_ACTIONS:
            raise ValueError(f"Invalid action: {action}")
        if model_name not in self.VALID_MODELS:
            raise ValueError(f"Invalid model name: {model_name}")
        return self._user.has_perm(f"core.{action}_{model_name}")


class HasAllTransactionPerm(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        perm_checker = PermChecker(request.user)
        user_has_perms = []
        for action in PermChecker.VALID_ACTIONS:
            user_has_perms.append(
                perm_checker.user_has_perm(
                    action, PermChecker.ALL_PERM_TRANSACTION_MODEL
                )
            )
        return all(user_has_perms)


class IsUserAdmin(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        user = request.user
        return user.role == RolesEnum.ADMIN and user.is_staff
