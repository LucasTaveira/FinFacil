from rest_framework import serializers

from ..models.incomes import UserIncome, UserIncomeItens

class UserIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncome
        fields = '__all__'

class UserIncomeItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncomeItens
        fields = '__all__'
