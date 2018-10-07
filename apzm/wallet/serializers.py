from rest_framework import serializers

from wallet.models import ClientWalletAccount, HistoryOperations, TradeWalletAccount


class HistoryOperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryOperations
        fields = ('id', 'successful_charge', 'successful_recharge', 'summary',
                  'created', 'modified')


class ClientWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWalletAccount
        fields = ('id', 'money', 'token', 'client')


class TradeWalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TradeWalletAccount
        fields = ('id', 'money', 'token', 'trade')

