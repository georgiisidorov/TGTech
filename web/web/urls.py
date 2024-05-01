"""web URL Configuration

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
from django.urls import path, include, re_path
from web.tgtech import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('oferta/', views.oferta, name='oferta'),
    path('cases/', views.cases, name='cases'),
    path('cases/posylochka/', views.posylochka, name='posylochka'),
    path('cases/happypc/', views.happypc, name='happypc'),
    # re_path(r'^eel/', include('django_eel.urls')), # do not alter this line
    # url(r'^tgtech/', include('tgtech.urls')), # set by your app name
]
