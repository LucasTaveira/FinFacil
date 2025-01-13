from django.urls import reverse
from rest_framework import status

from utils.tests.utils_class import FinFacilTestCase

from authentication.models import User
from control.models.incomes import UserIncome, UserIncomeItens

class UserIncomeTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.base_url = reverse('user-income-list')
        self.user_income = UserIncome.objects.create(
            user=self.user,
        )
    
    def test_get_user_income(self):
        "Should test sucess get user_income"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_fail_user_income(self):
        "Should test fail create user_income"
        
        data = {
            "user": self.user.id,
        }
        
        response = self.logged_django_client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class UserIncomeItensTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.base_url_itens = reverse('user-income-itens-list')
        self.user_income = UserIncome.objects.create(
            user=self.user,
        )
        self.user_income_itens = UserIncomeItens.objects.create(
            user_income=self.user_income,
            amount=100
        )
        self.user_income_itens2_ = UserIncomeItens.objects.create(
            user_income=self.user_income,
            amount=50
        )
        
        
    def test_get_user_income_itens(self):
        "Should test sucess get user_income_itens"
        
        response = self.logged_django_client.get(self.base_url_itens)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_user_income_itens(self):
        "Should test sucess create user_income_itens"
        
        data = {
            "user_income": self.user_income.id,
            "name": "salario",
            "amount": 100
        }
        
        response = self.logged_django_client.post(
            self.base_url_itens, 
            data, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_user_income_itens(self):
        "Should test sucess update user_income_itens"
        
        data = {
            "name": "salario",
            "amount": 1.00
        }
        
        response = self.logged_django_client.patch(
            f'{self.base_url_itens}{self.user_income_itens2_.id}/', 
            data, 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['amount']), data['amount'])
        
    def test_delete_user_income_itens(self):
        "Should test sucess delete user_income_itens"
        
        response = self.logged_django_client.delete(
            f'{self.base_url_itens}{self.user_income_itens.id}/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
