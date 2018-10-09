from rest_framework import routers

from wallet.api.v1.views import ClientApiViewSet, TradeApiViewSet

router = routers.SimpleRouter()
router.register(r'client', ClientApiViewSet)
router.register(r'trade', TradeApiViewSet)

urlpatterns = router.urls


# client_api = [
#     url(r'^client/(?P<pk>[0-9]+)/wallets/$', views.ClientWalletView.as_view()),
#     url(r'^client/(?P<pk>[0-9]+)/wallets/status$', views.ClientWalletStatusView.as_view()),
#     url(r'^client/(?P<pk>[0-9]+)/wallets/history-operations$', views.ClientWalletHistoryOperationsView.as_view()),
#     url(r'^client/(?P<pk>[0-9]+)/wallets/recharge$', views.ClientWalletRechargeView.as_view())
# ]
#
# trade_api = [
#     url(r'^trade/(?P<pk>[0-9]+)/wallets/$', views.TradeWalletView.as_view()),
#     url(r'^trade/(?P<pk>[0-9]+)/wallets/history-operations$', views.TradeWalletHistoryOperationsView.as_view()),
#     url(r'^trade/(?P<pk>[0-9]+)/wallets/charge', views.TradeWalletClientChargeView.as_view()),
# ]
#
# urlpatterns = client_api + trade_api
