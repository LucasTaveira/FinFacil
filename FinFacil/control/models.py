from django.db import models

from authentication.models import User

class UserIncome(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        user_income_itens = UserIncomeItens.objects.filter(
            user_income__id=self.id
        )
        if user_income_itens:
            total_amount = sum([i.amount for i in user_income_itens])
            self.amount = total_amount
        super().save()
    def __str__(self):
        return f'{self.id} - {self.user} - {self.amount}'


class UserIncomeItens(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False, 
        blank=False,
        default=0
    )
    user_income = models.ForeignKey(UserIncome, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id} - {self.name} - {self.amount}'
