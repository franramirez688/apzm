"""apzm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.conf import settings


API_VERSION = settings.API_CURRENT_VERSION
API_TITLE = 'WALLET API VERSION %s' % API_VERSION
API_DESCRIPTION = 'A Simple Web API for simulating a Wallet Web App'


urlpatterns = [
    url(r'^api/%s/' % API_VERSION, include(settings.API_CURRENT_VERSION_URLS_PATH)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]
