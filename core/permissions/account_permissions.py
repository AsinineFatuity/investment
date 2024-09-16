from typing import List
from django.contrib.auth.models import Permission, Group
from core.models import (
    User,
    PostOnlyTransaction,
    ViewOnlyTransaction,
    AllPermTransaction,
)


class AccountPermissions:
    VIEW_ONLY_PERMISSIONS = [
        "view_viewonlytransaction",
    ]  # perms for ViewOnlyAccount
    POST_ONLY_PERMISSIONS = [
        "add_postonlytransaction",
    ]  # perms for PostOnlyAccount
    ALL_PERM_PERMISSIONS = [
        "view_allpermtransaction",
        "add_allpermtransaction",
        "change_allpermtransaction",
        "delete_allpermtransaction",
    ]  # perms for AllPermAccount
    VIEW_ONLY_GRP = "view_only"
    POST_ONLY_GRP = "post_only"
    ALL_PERM_GRP = "all_perm"
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
        self._perm_created_grp_map = {
            self.VIEW_ONLY_GRP: [False, None],
            self.POST_ONLY_GRP: [False, None],
            self.ALL_PERM_GRP: [False, None],
        }
        self._view_only_group, self._post_only_group, self._all_perm_group = (
            self._get_or_create_groups()
        )
        for perm, (created, group) in self._perm_created_grp_map.items():
            if created:
                self._add_perm_to_groups(perm, group)
        self._user = user

    def _get_or_create_groups(self):
        view_only_group, view_created = Group.objects.get_or_create(
            name=self.VIEW_ONLY_GRP
        )
        post_only_group, post_created = Group.objects.get_or_create(
            name=self.POST_ONLY_GRP
        )
        all_perm_group, all_created = Group.objects.get_or_create(
            name=self.ALL_PERM_GRP
        )
        self._perm_created_grp_map[self.VIEW_ONLY_GRP] = [view_created, view_only_group]
        self._perm_created_grp_map[self.POST_ONLY_GRP] = [post_created, post_only_group]
        self._perm_created_grp_map[self.ALL_PERM_GRP] = [all_created, all_perm_group]
        return view_only_group, post_only_group, all_perm_group

    @staticmethod
    def _add_perm_to_groups(permissions: List[str], group: Group):
        perms = Permission.objects.filter(codename__in=permissions)
        group.permissions.add(*perms)

    def add_user_to_groups(self):
        user_groups = []
        for name, (created, group) in self._perm_created_grp_map.items():
            user_groups.append(group)
        self._user.groups.add(*user_groups)

    def user_has_perm(self, action: str, model_name: str):
        if action not in self.VALID_ACTIONS:
            raise ValueError(f"Invalid action: {action}")
        if model_name not in self.VALID_MODELS:
            raise ValueError(f"Invalid model name: {model_name}")
        return self._user.has_perm(f"core.{action}_{model_name}")
