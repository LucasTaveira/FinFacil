from django.urls import reverse
from rest_framework import status

from authentication.models import User
from utils.tests.utils_class import FinFacilTestCase

class UserTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.User = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.User2 = User.objects.create(
            first_name='first_name2', 
            authenticator=self.authenticator
        )
        self.base_url =  reverse('users-list')
        
    def test_create_user(self):
        "Should test sucess create user"
        
        data = {
            "first_name": "first_name",
            "authenticator": self.authenticator.id
        }
        
        response = self.client.post(self.base_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        assert response.data['first_name'] == data['first_name']
        
    def test_get_user(self):
        "Should test sucess get user"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_update_user(self):
        "Should test sucess update user"
        
        data = {
            "first_name": "test",
        }
        
        response = self.logged_django_client.patch(
            f'{self.base_url}{self.User.id}/', 
            data, 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(response.data['first_name'], data['first_name'])
    
    def test_delete_user(self):
        "Should test sucess delete user"
        
        response = self.logged_django_client.delete(f'{self.base_url}{self.User2.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    