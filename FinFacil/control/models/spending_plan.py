from django.db import models

from authentication.models import User

class SpendingPlan(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} - {self.user}'

class SpendingPlanItens(models.Model):
    name = models.CharField(
        null=False, 
        blank=False, 
        max_length=50
    )
    percent = models.SmallIntegerField(
        null=False, 
        blank=False,
        default=0
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False, 
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    spending_plan = models.ForeignKey(SpendingPlan, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} - {self.amount}'
