"""open_food_facts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers
from products.api import viewsets as products_viewsets
from account.api import viewsets as account_viewsets

route = routers.DefaultRouter()
route.register(r'users', account_viewsets.UserViewSet)
route.register(r'groups', account_viewsets.GroupViewSet)
route.register(r'products', products_viewsets.ProductsViewSet, basename="Products")

urlpatterns = [
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
