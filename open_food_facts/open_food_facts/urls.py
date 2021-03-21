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

# Django imports
from django.contrib import admin
from django.urls import path, include

# Django Rest Framework imports
from rest_framework import routers

# Account app imports
from account.api import viewsets as account_viewsets

route = routers.DefaultRouter()
route.register(r'users', account_viewsets.UserViewSet)
route.register(r'groups', account_viewsets.GroupViewSet)

urlpatterns = [
    path('', include('products.urls')),
    path('account/', include(route.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
