from django.urls import reverse
from rest_framework import status

from utils.tests.utils_class import FinFacilTestCase
from ..models.objective_list import ObjectiveList, ObjectiveListItens
from authentication.models import User

class ObjectiveListTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.ojective_list = ObjectiveList.objects.create(
            name="name",
            user=self.user
        )
        self.ojective_list_2 = ObjectiveList.objects.create(
            name="name_2",
            user=self.user
        )
        self.base_url = reverse('objective-list-list')

    def test_get_itens(self):
        "Should test sucess get objective list"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_itens(self):
        data = {
            "name": "name",
            "user": self.user.id
        }

        response = self.logged_django_client.post(
            self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_itens(self):
        data = {
            "name": "name_updated",
        }

        response = self.logged_django_client.patch(
            f'{self.base_url}{self.ojective_list.id}/', data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_itens(self):
        response = self.logged_django_client.delete(
            f'{self.base_url}{self.ojective_list_2.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ObjectiveListItensTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.base_url = reverse('objective-list-itens-list')
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.objective_list = ObjectiveList.objects.create(
            name='name',
            user=self.user
        )
        self.objective_list_itens = ObjectiveListItens.objects.create(
            name='name',
            amount=12,
            objective_list=self.objective_list
        )
        self.objective_list_itens_2 = ObjectiveListItens.objects.create(
            name='name_2',
            amount=12,
            objective_list=self.objective_list
        )
        
        
    def test_get_itens(self):
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_itens(self):
        data = {
            "name": "name",
            "amount": 12,
            "objective_list": self.objective_list.id
        }

        response = self.logged_django_client.post(
            self.base_url, data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_itens(self):
        data = {
            "name": "name_updated",
        }
        
        response = self.logged_django_client.patch(
            f'{self.base_url}{self.objective_list_itens.id}/', data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
    
    def test_delete_itens(self):
        response = self.logged_django_client.delete(
            f'{self.base_url}{self.objective_list_itens_2.id}/'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
