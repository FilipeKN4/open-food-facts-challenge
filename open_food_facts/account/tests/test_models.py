# Django imports
from django.contrib.auth.models import User

# Rest Framework imports
from rest_framework import status
from rest_framework.test import APITestCase


class TestUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            email='admin@mail.com',
            password='password123'
        )
        
        self.login()
    
    def login(self):
        self.client.force_authenticate(self.user)
        
    def test_user_login(self):
        self.client.logout()
        
        response = self.client.post('/api-auth/login/', {'username': 'admin', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_creation(self):
        data = {
            'username': 'test_user', 
            'email': 'test_user@mail.com',
            'password1': 'password123',
            'password1': 'password123'
        }
        
        response = self.client.post('/account/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    