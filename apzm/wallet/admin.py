from django.contrib import admin

from wallet.models import Trade, Client, TradeWalletAccount, ClientWalletAccount

admin.site.register(Client)
admin.site.register(Trade)
admin.site.register(TradeWalletAccount)
admin.site.register(ClientWalletAccount)
