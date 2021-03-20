from django.contrib.auth.models import User, Group
from rest_framework import serializers
from products import models


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'