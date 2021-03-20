from rest_framework import viewsets
from rest_framework import permissions
from products.api import serializers
from products import models


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()
    permission_classes = [permissions.IsAuthenticated]