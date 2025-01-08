from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import AuthenticationUser
class AuthenticatorTests(APITestCase):
    def setUp(self):
        self.Authenticator = AuthenticationUser.objects.create(
            email='email', 
            password='password'
        )
        self.base_url =  reverse('sign_in')
    def test_create_user(self):
        "Should test sucess create user"
        
        data = {
            "email": "test1@gmail.com",
            "password": "321"
        }
        
        response = self.client.post(self.base_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data['email'] == data['email']
        
    def test_create_user_fail(self):
        "Should test fail create user"
        
        data = {
            "email": 'email', 
            "password": 'password'
        }
        
        response = self.client.post(self.base_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
