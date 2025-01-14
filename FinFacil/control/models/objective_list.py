from django.db import models  

from authentication.models import User

class ObjectiveList(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} - {self.name} - {self.user}'


class ObjectiveListItens(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False, 
        blank=False,
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objective_list = models.ForeignKey(ObjectiveList, on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.id} - {self.name} - {self.amount} - {self.objective_list}'
