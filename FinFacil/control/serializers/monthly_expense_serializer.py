from rest_framework import serializers

from ..models.monthly_expense import MonthlyExpense, MonthlyExpenseItens

class MonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyExpense
        fields = '__all__'
        
class MonthlyExpenseItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyExpenseItens
        fields = '__all__'
