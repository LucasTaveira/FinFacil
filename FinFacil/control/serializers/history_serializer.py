from rest_framework import serializers

from ..models.history import (
    History,
    UserIncomeItensHistory,
    SpendingPlanItensHistory,
    MonthlyExpenseItensHistory,
    ObjectiveListItensHistory
)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"


class UserIncomeItensHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncomeItensHistory
        fields = "__all__"


class SpendingPlanItensHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendingPlanItensHistory
        fields = "__all__"


class MonthlyExpenseItensHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyExpenseItensHistory
        fields = "__all__"

class ObjectiveListItensHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectiveListItensHistory
        fields = "__all__"
