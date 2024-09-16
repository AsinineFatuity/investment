from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
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

    def __init__(self, user: User):
        self.view_only_group, self.post_only_group, self.all_perm_group = (
            self.get_or_create_groups()
        )
        pass

    def get_or_create_groups(self):
        view_only_group, created = Group.objects.get_or_create(name=self.VIEW_ONLY_GRP)
        post_only_group, created = Group.objects.get_or_create(name=self.POST_ONLY_GRP)
        all_perm_group, created = Group.objects.get_or_create(name=self.ALL_PERM_GRP)
        return view_only_group, post_only_group, all_perm_group

    def add_perm_to_groups(self):
        view_only_perms = Permission.objects.filter(
            codename__in=self.VIEW_ONLY_PERMISSIONS
        )
        pass
