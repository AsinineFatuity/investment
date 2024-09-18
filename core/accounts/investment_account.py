from core.models import AllPermAccount, PostOnlyAccount, ViewOnlyAccount, User


class InvestmentAccount:

    def __init__(self, user: User):
        self._investment_accounts = self._get_or_create_investment_accounts()
        self._user = user

    def _get_or_create_investment_accounts(self):
        all_perm, all_perm_created = AllPermAccount.objects.get_or_create()
        post_only, post_only_created = PostOnlyAccount.objects.get_or_create()
        view_only, view_only_created = ViewOnlyAccount.objects.get_or_create()
        return [all_perm, post_only, view_only]

    def add_user_to_investment_accounts(self):
        for account in self._investment_accounts:
            account.users.add(self._user)
