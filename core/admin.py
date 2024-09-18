from django.contrib import admin
from core.models import AllPermTransaction, PostOnlyTransaction, ViewOnlyTransaction

admin.site.register(AllPermTransaction)
admin.site.register(PostOnlyTransaction)
admin.site.register(ViewOnlyTransaction)
