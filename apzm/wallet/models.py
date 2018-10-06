import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    nif = models.IntegerField(unique=True, blank=False, db_index=True)


class Trade(AbstractUser):
    company_name = models.CharField(blank=False, max_length=128)
    cif = models.IntegerField(unique=True, blank=False, db_index=True)


class WalletAccount(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    money = models.IntegerField(null=True)

    trade = models.ForeignKey(Trade, related_name="wallet", db_index=True)
    client = models.ManyToManyField(Client,
                                    related_name="wallets")


class HistoryOperations(models.Model):
    successful_charge = models.BooleanField()
    successful_recharge = models.BooleanField()

    created = models.DateTimeField('Creation date', auto_now_add=True)
    modified = models.DateTimeField('Last modification date', auto_now=True)

    class Meta:
        abstract = True
