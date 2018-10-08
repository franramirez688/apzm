"""
    Helpers for creating test data
"""
from django.contrib.auth.models import User

from wallet.models import Trade, Client, TradeWalletAccount, \
    ClientWalletAccount


def create_wallet_clients():
    user1 = User.objects.create(
        username="sega"
    )
    user2 = User.objects.create(
        username="pedro"
    )
    trade = Trade.objects.create(
        company="Sega Saturn",
        cif="A5641565465",
        user=user1
    )
    client = Client.objects.create(
        nif="74895621X",
        user=user2
    )
    return client, trade


def create_wallet_accounts(client, trade):
    c_wallet = ClientWalletAccount.objects.create(
        money=150,
        client=client
    )
    t_wallet = TradeWalletAccount.objects.create(
        money=1560,
        trade=trade
    )
    return c_wallet, t_wallet
