from rest_framework import viewsets

from authentication.models import User
from ..models.monthly_expense import MonthlyExpense, MonthlyExpenseItens
from ..serializers.monthly_expense_serializer import MonthlyExpenseSerializer, MonthlyExpenseItensSerializer

class MonthlyExpenseView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MonthlyExpenseSerializer
    
    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return MonthlyExpense.objects.filter(
                user=self.request.user.authenticated_user
            )
        except User.DoesNotExist:
            return super().get_queryset()
    
class MonthlyExpenseItensView(viewsets.ModelViewSet):
    serializer_class = MonthlyExpenseItensSerializer
    
    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return MonthlyExpenseItens.objects.filter(
                monthly_expense__user=self.request.user.authenticated_user
            )
        except User.DoesNotExist:
            return super().get_queryset()
