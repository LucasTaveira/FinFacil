from rest_framework import viewsets

from ..models.history import (
    History, 
    UserIncomeItensHistory, 
    MonthlyExpenseItensHistory, 
    SpendingPlanItensHistory,
    ObjectiveListItensHistory
)
from ..serializers.history_serializer import (
    HistorySerializer,
    UserIncomeItensHistorySerializer,
    MonthlyExpenseItensHistorySerializer,
    SpendingPlanItensHistorySerializer,
    ObjectiveListItensHistorySerializer
)

class HistoryView(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    
    def get_queryset(self):
        try:
            if self.request.user.is_authenticated and self.request.user.is_staff:
                return History.objects.all()
        except History.DoesNotExist:
            return super().get_queryset()
    
class UserIncomeItensHistoryView(viewsets.ReadOnlyModelViewSet):
    queryset = UserIncomeItensHistory.objects.all()
    serializer_class = UserIncomeItensHistorySerializer
    
class MonthlyExpenseItensHistoryView(viewsets.ReadOnlyModelViewSet):
    queryset = MonthlyExpenseItensHistory.objects.all()
    serializer_class = MonthlyExpenseItensHistorySerializer 
    
class SpendingPlanItensHistoryView(viewsets.ReadOnlyModelViewSet):
    queryset = SpendingPlanItensHistory.objects.all()
    serializer_class = SpendingPlanItensHistorySerializer

class ObjectiveListItensHistoryView(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectiveListItensHistory.objects.all()
    serializer_class = ObjectiveListItensHistorySerializer
