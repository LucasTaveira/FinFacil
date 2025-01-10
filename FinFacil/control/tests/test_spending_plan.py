from django.urls import reverse
from rest_framework import status

from utils.tests.utils_class import FinFacilTestCase
from authentication.models import User
from ..models.spending_plan import SpendingPlan, SpendingPlanItens

class SpendingPlanTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.base_url = reverse('spending-plan-list')
        self.spending_plan = SpendingPlan.objects.create(
            user=self.user
        )

    def test_get_spending_plan(self):
        "Should test sucess get spending plan"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_spending_plan(self):
        "Should test sucess create spending plan"
        
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

class SpendingPlanItensTestCase(FinFacilTestCase):
    def setUp(self):
        super().setUp()
        
        self.user = User.objects.create(
            first_name='first_name', 
            authenticator=self.authenticator
        )
        self.base_url = reverse('spending-plan-itens-list')
        self.spending_plan = SpendingPlan.objects.create(
            user=self.user
        )
        self.spending_itens = SpendingPlanItens.objects.create(
            name='name',
            percent=100,
            amount=12.50,
            spending_plan=self.spending_plan
            
        )

    
    def test_get_spending_plan_itens(self):
        "Should test sucess get spending plan itens"
        
        response = self.logged_django_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_spending_plan_itens(self):
        "Should test sucess create spending plan itens"
        
        data = {
            "spending_plan": self.spending_plan.id,
            "name": "name",
            "percent": 100,
            "amount": 12.50
        }
        
        response = self.logged_django_client.post(
            self.base_url, data, 
            format='json'
        )
        self.assertEqual(
            response.status_code, 
            status.HTTP_201_CREATED
        )
        
    def test_update_spending_plan_itens(self):
        "Should test sucess update spending plan itens"
        
        data = {
            "name": "alterarde_name",
        }
        
        response = self.logged_django_client.patch(
            f'{self.base_url}{self.spending_itens.id}/', 
            data, 
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        
    def test_delete_spending_plan_itens(self):
        "Should test sucess delete spending plan itens"
        
        response = self.logged_django_client.delete(
            f'{self.base_url}{self.spending_itens.id}/'
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
