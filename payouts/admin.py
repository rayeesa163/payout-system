from django.contrib import admin
from .models import Merchant, LedgerEntry


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance')

    def balance(self, obj):
        return obj.get_balance()


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(LedgerEntry)

from .models import Payout
admin.site.register(Payout)
