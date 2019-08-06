"""mtvproject URL Configuration

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
# mtvproject/urls.py

from django.contrib import admin
from django.urls import path, include
import mtvapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mtvapp.views.home, name='home'),
    path('air/', mtvapp.views.air, name='air'),
    path('lodge/', mtvapp.views.lodge, name='lodge'),
    path('act/', mtvapp.views.act, name='act'),
    path('pak/', mtvapp.views.pak, name='pak'),
    path('trans/', mtvapp.views.trans, name='trans'),
    path('accounts/', include('accounts.urls')),
    path('new/', mtvapp.views.new, name='new'),
    path('create/', mtvapp.views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
