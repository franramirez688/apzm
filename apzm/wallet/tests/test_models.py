import uuid

from django.db import IntegrityError
from django.test import TestCase

from wallet.exceptions import WalletError
from wallet.models import Client, ClientWalletAccount, \
    TradeWalletAccount
from wallet.tests.factory import create_wallet_clients


class WalletAccountTestCase(TestCase):

    def setUp(self):
        self.client, self.trade = create_wallet_clients()

    def test_automatic_token_creation_client_wallet_account(self):
        c_wallet = ClientWalletAccount.objects.create(
            money=1456.23,
            client=self.client
        )
        self.assertTrue(c_wallet.token)

    def test_automatic_token_creation_trade_wallet_account(self):
        t_wallet = TradeWalletAccount.objects.create(
            money=1456.23,
            trade=self.trade
        )
        self.assertTrue(t_wallet.token)

    def test_one_client_can_have_several_wallet_accounts(self):
        ClientWalletAccount.objects.create(
            money=1456.23,
            client=self.client
        )
        ClientWalletAccount.objects.create(
            money=15.23,
            client=self.client
        )
        self.assertTrue(Client.objects.filter(pk=self.client.pk).count(), 2)

    def test_one_trade_can_have_only_one_wallet_accounts(self):
        with self.assertRaises(IntegrityError):
            TradeWalletAccount.objects.create(
                money=1000.23,
                trade=self.trade
            )
            TradeWalletAccount.objects.create(
                money=789,
                trade=self.trade
            )

    def test_recharge_any_wallet_account(self):
        c_wallet = ClientWalletAccount.objects.create(
            money=15,
            client=self.client
        )
        t_wallet = TradeWalletAccount.objects.create(
            money=30,
            trade=self.trade
        )
        c_wallet.recharge(40)
        t_wallet.recharge(40)

        self.assertEqual(c_wallet.money, 55)
        self.assertEqual(t_wallet.money, 70)

    def test_make_charge_by_one_trade_to_one_client_with_enough_money(self):
        c_wallet = ClientWalletAccount.objects.create(
            money=150,
            client=self.client
        )
        t_wallet = TradeWalletAccount.objects.create(
            trade=self.trade
        )
        t_wallet.make_a_client_charge(c_wallet.token, 100)

        c_wallet.refresh_from_db()
        self.assertEqual(c_wallet.money, 50)
        self.assertEqual(t_wallet.money, 100)

    def test_make_charge_by_one_trade_to_one_client_with_not_enough_money(self):
        c_wallet = ClientWalletAccount.objects.create(
            money=20,
            client=self.client
        )
        t_wallet = TradeWalletAccount.objects.create(
            trade=self.trade
        )
        t_wallet.make_a_client_charge(c_wallet.token, 100)

        self.assertEqual(c_wallet.money, 20)
        self.assertIsNone(t_wallet.money)

    def test_make_charge_by_one_trade_to_non_existing_client(self):
        t_wallet = TradeWalletAccount.objects.create(
            trade=self.trade
        )
        self.assertRaises(WalletError, t_wallet.make_a_client_charge, uuid.uuid4(), 100)


class OperationsWalletAccountTestCase(TestCase):
    pass
