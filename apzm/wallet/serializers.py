from rest_framework import serializers

from wallet.models import ClientWalletAccount, HistoryOperations, TradeWalletAccount, Client, Trade


class HistoryOperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryOperations
        fields = ('id', 'successful_charge', 'successful_recharge', 'summary',
                  'created')


class ClientWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWalletAccount
        fields = ('id', 'money', 'token', 'client')


class TradeWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeWalletAccount
        fields = ('id', 'money', 'token', 'trade')


class ClientSerializer(serializers.ModelSerializer):
    client_wallets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('user', 'nif', 'client_wallets')


class TradeSerializer(serializers.ModelSerializer):
    trade_wallets = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Trade
        fields = ('user', 'cif', 'company', 'trade_wallets')
