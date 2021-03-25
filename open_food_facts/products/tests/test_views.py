# Django imports
from django.contrib.auth.models import User
from django.urls import reverse

# Rest Framework imports
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient, APIRequestFactory, RequestsClient

# Products imports
from products.models import Products, ProductsUpdateHistory


class TestProductsAPIViews(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            email='admin@mail.com',
            password='password123'
        )
        self.product = Products.objects.create(
            code='00000033333',
            status='draft',
            creator='filipe',
            product_name='chocolate'
        )
        self.products_update_history = ProductsUpdateHistory.objects.create(
            created_products = 1,
            updated_products = 0,
            deleted_products = 0
        )
        self.login()
        
    def login(self):
        self.client.force_authenticate(self.user)
        
    def test_api_details(self): 
        response = self.client.get(reverse('api_details'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_products_overview(self): 
        response = self.client.get(reverse('products_overview'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_products_list(self): 
        response = self.client.get(reverse('products_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_product_detail(self): 
        response = self.client.get(reverse('product_detail', args=[self.product.code]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_products_update_history_list(self): 
        response = self.client.get(reverse('products_update_history_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_products_update_history_detail(self): 
        response = self.client.get(reverse('products_update_history_detail', args=[self.products_update_history.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)