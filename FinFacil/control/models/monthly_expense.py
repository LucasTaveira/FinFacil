from django.db import models

from authentication.models import User

class MonthlyExpense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id} - {self.user}'
    
class MonthlyExpenseItens(models.Model):
    class TypeMonthlyExpenseItens(models.TextChoices):
        fixed = 'F', 'FIXED'
        variable = 'V', 'VARIABLE'
    
    name = models.CharField(max_length=50, null=False, blank=False)
    obs = models.CharField(max_length=50)
    value = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False, 
        blank=False
    )
    due_date = models.PositiveSmallIntegerField()
    amount_sum = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    amount_paid = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    dif_amount_paid = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text="amount_sum field - amount_paid field"
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    type_expense = models.CharField(
        choices=TypeMonthlyExpenseItens.choices, 
        default=TypeMonthlyExpenseItens.fixed,
        max_length=1
    )
    monthly_expense = models.ForeignKey(MonthlyExpense, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} - {self.name} - {self.type_expense} - {self.monthly_expense}'
