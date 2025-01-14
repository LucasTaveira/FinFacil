from django.urls import reverse
from rest_framework import status

from utils.tests.utils_class import FinFacilTestCase

from authentication.models import User
from ..models.history import (
    History)
from ..models.incomes import UserIncomeItens, UserIncome
from ..models.monthly_expense import MonthlyExpenseItens, MonthlyExpense
from ..models.spending_plan import SpendingPlanItens, SpendingPlan

class HistoryTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.url_base = reverse('history-list')
        self.history = History.objects.create(
            update={"amount": 12.50}
        )
        self.hisotry_2 = History.objects.create(
            update={"amount": 12.50}
        )

    def test_get_itens(self):
        response = self.logged_django_client_admin.get(self.url_base)
        self.assertAlmostEqual(
            response.status_code, status.HTTP_200_OK)
        
    def test_create(self):
        data = {
            'update': {"amount": 12.50}
        }

        response = self.logged_django_client_admin.post(
            self.url_base, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        data = {
            'update': {"amount": 9.50}
        }

        response = self.logged_django_client_admin.patch(
            f'{self.url_base}{self.history.id}/', data, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['update'], data['update'])
        
    def test_delete(self):
        response = self.logged_django_client_admin.delete(
            f'{self.url_base}{self.hisotry_2.id}/', self.url_base)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class UserIncomeItensHistoryTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.url_base = reverse('user-income-itens-history-list')
        self.history = History.objects.create(
            update={"amount": 12.50}
        )
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.user_income = UserIncome.objects.create(
            user=self.user
        )
        self.user_income_itens = UserIncomeItens.objects.create(
            user_income=self.user_income,
            name='name',
            amount=12.50
        )
    def test_get_itens(self):
        response = self.logged_django_client.get(self.url_base)
        self.assertAlmostEqual(
            response.status_code, status.HTTP_200_OK)

    def test_create_fail(self):
        data = {
            'history': self.history,
            'user_income_itens': self.user_income_itens
        }

        response = self.logged_django_client.post(self.url_base, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class SpendingPlanItensHistoryTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.url_base = reverse('spending-plan-itens-history-list')
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.history = History.objects.create(
            update={"amount": 12.50}
        )
        self.spending_plan = SpendingPlan.objects.create(
            user=self.user
        )
        self.spending_plan_itens = SpendingPlanItens.objects.create(
            name='name',
            percent=100,
            amount=12.50,
            spending_plan=self.spending_plan
        )

    def test_get_itens(self):
        response = self.logged_django_client.get(self.url_base)
        self.assertAlmostEqual(
            response.status_code, status.HTTP_200_OK)

    def test_create_fail(self):
        data = {
            'history': self.history,
            'spending_plan_itens': self.spending_plan_itens
        }

        response = self.logged_django_client.post(self.url_base, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class MonthlyExpenseItensHistoryTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.url_base = reverse('monthly-expense-itens-history-list')   
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.history = History.objects.create(
            update={"amount": 12.50}
        )
        self.monthly_expense = MonthlyExpense.objects.create(
            user=self.user
        )
        self.monthly_expense_itens = MonthlyExpenseItens.objects.create(
            monthly_expense=self.monthly_expense,
            name='name',
            value=12.50,
            due_date=12
        )
            
    def test_get_itens(self):
        response = self.logged_django_client.get(self.url_base)
        self.assertAlmostEqual(
            response.status_code, status.HTTP_200_OK)

    def test_create_fail(self):
        data = {
            'history': self.history,
            'monthly_expense_itens': self.monthly_expense_itens
        }

        response = self.logged_django_client.post(self.url_base, data)
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
