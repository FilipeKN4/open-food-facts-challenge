# Libs imports
import json
import requests
import datetime
from decimal import Decimal

# Django imports
from django.utils.timezone import make_aware
from django.http import HttpResponse, Http404

# Django Rest Framework imports
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework import generics

# Products app imports
from products.models import Products
from products.api.serializers import ProductsSerializer

    
# Consume Open Food Facts API method
def get_product(code):  
    url = 'https://world.openfoodfacts.org/api/v0/product/{}.json'.format(code)
    
    response = requests.get(url)
    product = json.loads(response.content) if response.status_code == 200 else []
    
    return product


# Update a product instance
def update_product(product_json, product):
    product.status = product.Status.published
    product.imported_t = datetime.datetime.now()
    product.url = product_json.get('url') if product_json.get('url') else ''
    product.creator = product_json.get('creator') if product_json.get('creator') else ''
    product.created_t = make_aware(datetime.datetime.fromtimestamp(int(product_json.get('created_t'))))
    product.last_modified_t = make_aware(datetime.datetime.fromtimestamp(int(product_json.get('last_modified_t'))))
    product.product_name = product_json.get('product_name') if product_json.get('product_name') else ''
    product.quantity = product_json.get('quantity') if product_json.get('quantity') else ''
    product.brands = product_json.get('brands') if product_json.get('brands') else ''
    product.categories = product_json.get('categories') if product_json.get('categories') else ''
    product.labels = product_json.get('labels') if product_json.get('labels') else ''
    product.cities = product_json.get('cities') if product_json.get('cities') else ''
    product.purchase_places = product_json.get('purchase_places') if product_json.get('purchase_place') else ''
    product.stores = product_json.get('stores') if product_json.get('stores') else ''
    product.ingredients_text = product_json.get('ingredients_text') if product_json.get('ingredients_text') else ''
    product.traces = product_json.get('traces') if product_json.get('traces') else ''
    product.serving_size = product_json.get('serving_size') if product_json.get('serving_size') else ''
    product.serving_quantity = 0 if product_json.get('serving_quantity') is None or '' else Decimal(product_json.get('serving_quantity'))
    product.nutriscore_score = 0 if product_json.get('nutriscore_score') is None or '' else int(product_json.get('nutriscore_score'))
    product.nutriscore_grade = product_json.get('nutriscore_grade') if product_json.get('nutriscore_grade') else ''
    product.main_category = product_json.get('main_category') if product_json.get('main_category') else ''
    product.image_url = product_json.get('image_url') if product_json.get('image_url') else ''
    product.save()
    
    return product
   
   
# API classes for endpoints
class ProductsOverview(APIView):
    """
    Products endpoints overview.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        products_urls = {
            'List':'/products/',
            'Detail':'/products/<str:code>',
            'Update':'/products/<str:code>',
            'Delete':'/products/<str:code>',
        }
    
        return Response(products_urls)

class ProductsList(generics.ListAPIView):
    """
    List all products.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticated]


class ProductDetail(APIView):
    """
    Retrieve, update or delete a product instance.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self, code):
        try:
            return Products.objects.get(code=code)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, code, format=None):
        product = self.get_object(code)
        print(product)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def put(self, request, code, format=None):
        product = self.get_object(code)
        data = get_product(code)
        if data:
            product_json = data.get('product')
            product = update_product(product_json, product)
            serializer = ProductsSerializer(product)
            return Response(serializer.data)
        return HttpResponse(status=404)

    def delete(self, request, code, format=None):
        product = self.get_object(code)
        product.status = product.Status.trash
        product.save()
        serializer = ProductsSerializer(product)
        return Response(serializer.data)