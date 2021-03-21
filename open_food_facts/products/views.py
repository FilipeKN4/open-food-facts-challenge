import json
import requests
import datetime
from decimal import Decimal
from django.utils.timezone import make_aware
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Products
from products.api.serializers import ProductsSerializer


# Consume Open Food Facts API methods
def get_product(request, code):  
    url = 'https://world.openfoodfacts.org/api/v0/product/{}.json'.format(code)
    
    response = requests.get(url)
    product = json.loads(response.content) if response.status_code == 200 else ''
    
    return product
    

# API endpoints methods
@api_view(['GET'])
def products_overview(request):
    products_urls = {
        'List':'/products/',
        'Detail':'/products/<str:code>',
        'Update':'/products/<str:code>',
        'Delete':'/products/<str:code>',
    }
    
    return Response(products_urls)

@api_view(['GET'])
def products_list(request):
    """
    List all products.
    """
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, code):
    """
    Retrieve, Update or Delete a product.
    """
    try:
        product = Products.objects.get(code=code)
    except Products.DoesNotExist:
        return HttpResponse(status=404)
    
    serializer = ProductsSerializer(product)
    if request.method == 'GET':
        return Response(serializer.data)
    
    if request.method == 'PUT':
        data = get_product(request, code)
        if data:
            product_json = data.get('product')

            product.status = product.Status.published
            product.imported_t = datetime.datetime.now()
            product.url = product_json.get('url')
            product.creator = product_json.get('creator') 
            product.created_t = make_aware(datetime.datetime.fromtimestamp(int(product_json.get('created_t'))))
            product.last_modified_t = make_aware(datetime.datetime.fromtimestamp(int(product_json.get('last_modified_t'))))
            product.product_name = product_json.get('product_name') 
            product.quantity = product_json.get('quantity') 
            product.brands = product_json.get('brands') 
            product.categories = product_json.get('categories') 
            product.labels = product_json.get('labels') 
            product.cities = product_json.get('cities') 
            product.purchase_places = product_json.get('purchase_places') 
            product.stores = product_json.get('stores') 
            product.ingredients_text = product_json.get('ingredients_text') 
            product.traces = product_json.get('traces') 
            product.serving_size = product_json.get('serving_size') 
            product.serving_quantity = 0 if product_json.get('serving_quantity') is None or '' else Decimal(product_json.get('serving_quantity'))
            product.nutriscore_score = 0 if product_json.get('nutriscore_score') is None or '' else int(product_json.get('nutriscore_score'))
            product.nutriscore_grade = product_json.get('nutriscore_grade') 
            product.main_category = product_json.get('main_category') 
            product.image_url = product_json.get('image_url') 
            product.save()
            
            return Response(serializer.data)
        return HttpResponse(status=404)
    
    if request.method == 'DELETE':
        product.status = product.Status.trash
        product.save()
        return Response(serializer.data)