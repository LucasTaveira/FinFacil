from rest_framework import viewset

from .models import UserIncome, UserIncomeItens
from .serializers import UserIncomeSerializer, UserIncomeItensSerializer

class UserIncomeView(viewset.ModelViewSet):
    queryset = UserIncome.objects.all()
    serializer_class = UserIncomeSerializer

class UserIncomeItensView(viewset.ModelViewSet):
    queryset = UserIncomeItens.objects.all()
    serializer_class = UserIncomeItensSerializer