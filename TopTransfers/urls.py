"""TopTransfers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('players/', players),
    path('latest-transfers/', transfers),
    path('clubs/', clubs),
    path('tryouts/', tryouts),
    path('about/', about),
    path('transfer-archive/', archive),
    path('season/<str:s>/', seasons),
    path('country/<str:s>/', country),
    path('country-clubs/<str:s>/', countryclubs),
    path('U20-players/', u20players),
    path('stats/', stats),
    path('stats/transfer-records/', transfer_records),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
