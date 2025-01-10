from rest_framework import serializers

from ..models.spending_plan import SpendingPlan, SpendingPlanItens

class SpendingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingPlan
        fields = '__all__'

class SpendingPlanItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingPlanItens
        fields = '__all__'
