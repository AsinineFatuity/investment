from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from core.models import User, ViewOnlyAccount, AllPermAccount, PostOnlyAccount


class CreateAccountPermissions:
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

    def __init__(self, user: User):
        pass

    def create_perm_groups(self):
        pass
