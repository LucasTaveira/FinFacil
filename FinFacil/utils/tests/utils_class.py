import random
import string

from django.urls import reverse
from django.test import Client as DjangoClient
from django.core.cache import cache

from rest_framework.test import APITestCase

from authentication.models import AuthenticationUser

class FinFacilTestCase(APITestCase):
    def setUp(self):
        cache.clear()
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        self.authenticator = AuthenticationUser.objects.create(
            email='usertest@gmail.com', 
            password=password
        )
        self.login_url = reverse('token_obtain_pair')

        self.django_client = DjangoClient()
        self.django_client.login(email=self.authenticator.email, password=password)
        login_data = {"email": self.authenticator.email, "password": password}
        
        token = self.django_client.post(self.login_url, data=login_data)
        self.access_token = token.data.get('access')
        
        self.logged_django_client = DjangoClient(
            headers={
                'Authorization': f'Bearer {self.access_token}'}
        )
        self.logged_django_client.login(email=self.authenticator.email, password=password)
        