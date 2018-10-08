from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wallet.models import ClientWalletAccount, HistoryOperations
from wallet.serializers import ClientWalletSerializer, HistoryOperationsSerializer, TradeWalletSerializer


def get_client_wallet_object(pk, token):
    try:
        client_wallet = ClientWalletAccount.objects.get(
            token=token,
            client=pk
        )
    except ClientWalletAccount.DoesNotExist:
        raise status.HTTP_404_NOT_FOUND
    else:
        return client_wallet


class ClientWalletView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def post(self, request, pk, format=None):
        data = request.data
        data['client'] = pk
        serializer = ClientWalletSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientWalletStatusView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get(self, request, pk):
        client_wallet = ClientWalletAccount.objects.filter(client=pk)
        serializer = ClientWalletSerializer(client_wallet, many=True)
        return Response(serializer.data)


class ClientWalletHistoryOperationsView(APIView):

    def get(self, request, pk):
        token = request.GET.get('token')
        ops_filter = Q(clientwalletaccount_operations__client=pk)
        if token:
            ops_filter &= Q(clientwalletaccount_operations__token=token)

        ops = HistoryOperations.objects.filter(ops_filter)
        serializer = HistoryOperationsSerializer(ops, many=True)
        return Response(serializer.data)


class ClientWalletRechargeView(APIView):

    def put(self, request, pk):
        data = request.data
        data['client'] = pk
        serializer = ClientWalletSerializer(data=data)
        if serializer.is_valid():
            client_wallet = get_client_wallet_object(pk, serializer.data['token'])
            client_wallet.charge(serializer.data['money'])
            return Response({'status': 'successfull wallet account recharge'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class TradeWalletView(APIView):

    def post(self, request, pk, format=None):
        data = request.data
        data['trade'] = pk
        serializer = TradeWalletSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TradeWalletClientChargeView(APIView):

    def put(self, request, pk, format=None):
        data = request.data
        data['trade'] = pk
        serializer = TradeWalletSerializer(data=data)
        if serializer.is_valid():
            trade_wallet = ClientWalletAccount.objects.get(trade=pk)
            trade_wallet.make_a_client_charge(data['client_token'],
                                              serializer.data['money'])
            return Response({'status': 'successfull client wallet account charge'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TradeWalletHistoryOperationsView(APIView):

    def get(self, request, pk):
        token = request.GET.get('token')
        ops_filter = Q(tradewalletaccount_operations__trade=pk)
        if token:
            ops_filter &= Q(tradewalletaccount_operations__token=token)

        ops = HistoryOperations.objects.filter(ops_filter)
        serializer = HistoryOperationsSerializer(ops, many=True)
        return Response(serializer.data)
