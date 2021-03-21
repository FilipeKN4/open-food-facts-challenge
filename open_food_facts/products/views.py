import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from products.models import Products
from products.serializers import ProductsSerializer


# Consume Open Food Facts API methods
def get_product(request, code):  
    url = 'https://world.openfoodfacts.org/api/v0/product/{}.json'.format(code)
    
    response = requests.get(url)
    product = response.json()
    
    return JsonResponse(product)
    

# API endpoints methods
@api_view(['GET',])
def products_list(request):
    """
    List all code products, or create a new product.
    """
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    

@api_view(['GET', ])
def product_detail(request, pk):
    """
    Retrieve a code product.
    """
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ProductsSerializer(product)
    return JsonResponse(serializer.data)


@api_view(['PUT', ])
def product_detail(request, pk):
    """
    Update a code product.
    """
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse(status=404)
    
    data = JSONParser().parse(request)
    serializer = ProductsSerializer(product, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


# @api_view(['DELETE', ])
# def product_detail(request, pk):
#     """
#     Set a trash status to a code product.
#     """
#     try:
#         product = Products.objects.get(pk=pk)
#     except Products.DoesNotExist:
#         return HttpResponse(status=404)
    
    
