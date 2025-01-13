from django.urls import reverse
from rest_framework import status

from utils.tests.utils_class import FinFacilTestCase
from authentication.models import User
from control.models.monthly_expense import MonthlyExpenseItens, MonthlyExpense

class MonthlyExpenseTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        
        self.base_url = reverse('monthly-expense-list')
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        
    def test_get_monthly_expense(self):
        "Should test sucess get monthly_expense"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_fail_create_monthly_expense(self):
        "Should test fail create monthly_expense"
        
        data = {
            "user": self.user.id,
        }
        
        response = self.logged_django_client.post(
            self.base_url, data, 
            format='json'
        )
        self.assertEqual(
            response.status_code, 
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

class MonthlyExpenseItensTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        
        self.base_url = reverse('monthly-expense-itens-list')
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.monthly_expense = MonthlyExpense.objects.create(
            user=self.user
        )
        self.monthly_expense_itens = MonthlyExpenseItens.objects.create(
            name='name',
            value=12.50,
            due_date=12,
            monthly_expense=self.monthly_expense
        )
        self.monthly_expense_itens_2 = MonthlyExpenseItens.objects.create(
            name='name',
            value=12.50,
            due_date=12,
            monthly_expense=self.monthly_expense
        )
        
    def test_get_monthly_expense_itens(self):
        "Should test sucess get monthly_expense_itens"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_monthly_expense_itens(self):
        "Should test sucess create monthly_expense_itens"
        
        data = {
            "name": "name created",
            "value": 12.50,
            "due_date": 12,
            "monthly_expense": self.monthly_expense.id
        }
        
        response = self.logged_django_client.post(
            self.base_url, data, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        
    def test_update_monthly_expense_itens(self):
        "Should test sucess update monthly_expense_itens"
        
        data = {
            "name": "alterarde_name",
        }
        
        response = self.logged_django_client.patch(
            f'{self.base_url}{self.monthly_expense_itens.id}/', 
            data, 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        
    def test_delete_monthly_expense_itens(self):
        "Should test sucess delete monthly_expense_itens"
        
        response = self.logged_django_client.delete(
            f'{self.base_url}{self.monthly_expense_itens_2.id}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
