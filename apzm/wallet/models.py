import uuid

from django.contrib.auth.models import User
from django.db import models, transaction, DatabaseError

from wallet.exceptions import ClientWalletAccountEmpty, WalletError


class ClientBase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    is_client = models.BooleanField(default=False)
    is_trade = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Client(ClientBase):
    nif = models.CharField(unique=True, blank=False, null=False,
                           db_index=True, max_length=10)
    is_client = models.BooleanField(default=True)


class Trade(ClientBase):
    company = models.CharField(blank=False, max_length=64)
    cif = models.CharField(unique=True, blank=False, null=False,
                           db_index=True, max_length=32)
    is_trade = models.BooleanField(default=True)


class HistoryOperations(models.Model):
    successful_charge = models.BooleanField(null=True)
    successful_recharge = models.BooleanField(null=True)
    summary = models.TextField(null=True, blank=True)

    created = models.DateTimeField('Creation date', auto_now_add=True)
    modified = models.DateTimeField('Last modification date', auto_now=True)


class WalletAccountBase(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    money = models.FloatField(blank=False, null=True)

    operations = models.ManyToManyField(HistoryOperations,
                                        blank=False,
                                        related_name="%(class)s_operations")
    class Meta:
        abstract = True

    def recharge(self, money):
        self.money = money if self.money is None else self.money + money
        op = HistoryOperations.objects.create(
            successful_recharge=True,
            summary="Successful recharge of %s euros" % self.money
        )
        self.operations.add(op)
        self.save()


class ClientWalletAccount(WalletAccountBase):
    client = models.ForeignKey(Client, related_name="client_wallet",
                               db_index=True, on_delete=models.CASCADE)

    def charge(self, money):
        if self.money is None or (self.money - money) < 0:
            op = HistoryOperations.objects.create(
                successful_charge=False,
                summary="Failing charge of %s euros. The account has not "
                        "enough money" % self.money
            )
            self.operations.add(op)
            raise ClientWalletAccountEmpty("It could not make the charge."
                                           "Empty account or with not enough "
                                           "money")
        self.money -= money
        self.save()


class TradeWalletAccount(WalletAccountBase):
    trade = models.OneToOneField(Trade, related_name="trade_wallet", db_index=True,
                                 on_delete=models.CASCADE)

    def make_a_client_charge(self, client_wallet_token, money):
        try:
            client_wallet = ClientWalletAccount.objects.get(token=client_wallet_token)
        except ClientWalletAccount.DoesNotExist:
            raise WalletError("Does not exist a client wallet account with "
                              "the token %s" % client_wallet_token)

        try:
            client_wallet.charge(money)
        except ClientWalletAccountEmpty:
            op = HistoryOperations.objects.create(
                successful_charge=False,
                summary="Failing client charge of %s euros."
                        "His/Her account has not enough money" % self.money
            )
            self.operations.add(op)
        else:
            # Supposing that the money should go to our trade account
            self.recharge(money)
