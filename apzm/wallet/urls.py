from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from wallet import views


urlpatterns = [
    url(r'^api/v1/client/(?P<pk>[0-9]+)/wallets/$', views.ClientWalletView.as_view()),
    url(r'^api/v1/client/(?P<pk>[0-9]+)/wallets/status$', views.ClientWalletStatusView.as_view()),
    url(r'^api/v1/client/(?P<pk>[0-9]+)/wallets/history-operations$', views.ClientWalletHistoryOperationsView.as_view()),
    url(r'^api/v1/client/(?P<pk>[0-9]+)/wallets/recharge$', views.ClientWalletRechargeView.as_view()),
    url(r'^api/v1/trade/(?P<pk>[0-9]+)/wallets/$', views.TradeWalletView.as_view()),
    url(r'^api/v1/trade/(?P<pk>[0-9]+)/wallets/history-operations$', views.TradeWalletHistoryOperationsView.as_view()),
    url(r'^api/v1/trade/(?P<pk>[0-9]+)/wallets/charge', views.TradeWalletClientChargeView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
