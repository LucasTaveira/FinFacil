from rest_framework import viewsets

from authentication.models import User
from ..models.spending_plan import SpendingPlan, SpendingPlanItens
from ..serializers.spending_plan_serializer import (
    SpendingPlanSerializer, 
    SpendingPlanItensSerializer
)

class SpendingPlanView(viewsets.ReadOnlyModelViewSet):
    serializer_class = SpendingPlanSerializer

    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return SpendingPlan.objects.filter(
                user=self.request.user.authenticated_user
            )
        except User.DoesNotExist:
            return super().get_queryset()
    

class SpendingPlanItensView(viewsets.ModelViewSet):
    serializer_class = SpendingPlanItensSerializer
    
    def get_queryset(self):
        try:
            self.request.user.is_authenticated
            return SpendingPlanItens.objects.filter(
                spending_plan__user=self.request.user.authenticated_user
            )
        except User.DoesNotExist:
            return super().get_queryset()
