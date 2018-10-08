from rest_framework.test import APITestCase, APIClient

from wallet.tests.factory import create_wallet_clients, create_wallet_accounts


class _BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.client, self.trade = create_wallet_clients()
        self.c_wallet, self.t_wallet = create_wallet_accounts(self.client,
                                                              self.trade)


class ClientApiTestCase(APITestCase):
    client = APIClient()

    def test_can_login(self):
        pass

    def test_can_logout(self):
        pass


class TradeApiTestCase(APITestCase):
    client = APIClient()

    def test_can_login(self):
        pass

    def test_can_logout(self):
        pass


class ClientWalletAccountApiTestCase(_BaseViewTest):

    def test_create_wallet_accounts(self):
        """Client user can create several wallet accounts"""
        pass

    def test_get_all_account_status(self):
        """Any client can list all his/her status accounts"""
        pass

    def test_has_not_perms_to_list_other_client_accounts(self):
        """Any client can not list not belonging status accounts"""
        pass

    def test_get_all_history_operations(self):
        """Any client can list all his/her history operations accounts"""
        pass

    def test_has_not_perms_to_list_other_client_history_operations(self):
        """Any client can not list not belonging history operations accounts"""
        pass

    def test_recharge_account(self):
        """Any client can recharge all his/her wallet accounts"""
        pass

    def test_has_not_perms_to_recharge_any_other_client_account(self):
        """Any client can not recharge not belonging accounts"""
        pass


class TradeWalletAccountApiTestCase(_BaseViewTest):

    def test_create_wallet_account(self):
        """Trade user can create wallet account"""
        pass

    def test_get_all_history_operations(self):
        """Any trade can list all his/her history operations accounts"""
        pass

    def test_has_not_perms_to_list_other_client_history_operations(self):
        """Any trade can not list not belonging history operations accounts"""
        pass

    # FIXME: Any client? any perms? any control?
    def test_make_a_client_charge(self):
        """Any trade can make a charge to another client user"""
        pass
