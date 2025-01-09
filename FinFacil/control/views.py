from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import User, UserIncome, UserIncomeItens
from .serializers import UserIncomeSerializer, UserIncomeItensSerializer

class UserIncomeView(viewsets.ReadOnlyModelViewSet):
    queryset = UserIncome.objects.all()
    serializer_class = UserIncomeSerializer
    
    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return UserIncome.objects.filter(
                user=self.request.user.authenticated_user
                )
        except User.DoesNotExist:
            return super().get_queryset()

class UserIncomeItensView(viewsets.ModelViewSet):
    serializer_class = UserIncomeItensSerializer
    
    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return UserIncomeItens.objects.filter(
                user_income__user=self.request.user.authenticated_user
            )
        except User.DoesNotExist:
            return super().get_queryset()
