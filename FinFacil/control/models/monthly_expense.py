from django.db import models
from authentication.models import User


class MonthlyExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    @property
    def amount_sum(self):
        monthly_itens = MonthlyExpenseItens.objects.filter(monthly_expense__id=self.id)
        return sum([item.value for item in monthly_itens])
    
    @property
    def amount_paid(self):
        user_itens = MonthlyExpenseItens.objects.filter(monthly_expense__id=self.id)
        return sum([item.amount_paid for item in user_itens])
    @property
    def dif_amount_paid(self):
        return self.amount_sum - self.amount_paid

    def __str__(self):
        return f"{self.id} - {self.user}"


class MonthlyExpenseItens(models.Model):
    class TypeMonthlyExpenseItens(models.TextChoices):
        fixed = "F", "FIXED"
        variable = "V", "VARIABLE"

    name = models.CharField(max_length=50, null=False, blank=False)
    obs = models.CharField(max_length=50, null=True, blank=True)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    due_date = models.PositiveSmallIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(
        default=False, help_text="True = paid, False = not paid")
    type_expense = models.CharField(
        choices=TypeMonthlyExpenseItens.choices,
        default=TypeMonthlyExpenseItens.fixed,
        max_length=1,
    )
    monthly_expense = models.ForeignKey(MonthlyExpense, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.type_expense}"
