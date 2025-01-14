from django.db import models

from .incomes import UserIncomeItens
from .monthly_expense import MonthlyExpenseItens
from .spending_plan import SpendingPlanItens
from .objective_list import ObjectiveListItens

class History(models.Model):
    update = models.JSONField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserIncomeItensHistory(models.Model):
    user_income_itens = models.ForeignKey(UserIncomeItens, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SpendingPlanItensHistory(models.Model):
    spending_plan_itens = models.ForeignKey(SpendingPlanItens, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MonthlyExpenseItensHistory(models.Model):
    monthly_expense_itens = models.ForeignKey(MonthlyExpenseItens, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ObjectiveListItensHistory(models.Model):
    objective_list_itens = models.ForeignKey(ObjectiveListItens, on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
