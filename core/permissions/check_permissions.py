from core.models import (
    ViewOnlyTransaction,
    PostOnlyTransaction,
    AllPermTransaction,
    User,
)


class CheckPermissions:
    # Define possible actions
    VIEW_ACTION = "view"
    ADD_ACTION = "add"
    CHANGE_ACTION = "change"
    DELETE_ACTION = "delete"
    VALID_ACTIONS = [VIEW_ACTION, ADD_ACTION, CHANGE_ACTION, DELETE_ACTION]
    VALID_MODELS = [
        ViewOnlyTransaction.__name__.lower(),
        PostOnlyTransaction.__name__.lower(),
        AllPermTransaction.__name__.lower(),
    ]

    def __init__(self, user: User):
        self._user = user

    def user_has_perm(self, action: str, model_name: str):
        if action not in self.VALID_ACTIONS:
            raise ValueError(f"Invalid action: {action}")
        if model_name not in self.VALID_MODELS:
            raise ValueError(f"Invalid model name: {model_name}")
        return self._user.has_perm(f"core.{action}_{model_name}")
