from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthenticationUser(AbstractUser):

    email = models.EmailField(null=False, blank=False, unique=True)
    superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    username = models.CharField(max_length=1, blank=True, null=True, unique=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    def save(self, *args, **kwargs):
        if self.pk is None or 'password' in self.__dict__ and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super().save(*args, **kwargs)
        

class User(models.Model):
    class UserType(models.TextChoices):
        user = 'U', 'USER'
        api = 'A', 'API'       
        
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    whatsApp = models.CharField(max_length=30, null=True, blank=True)
    user_type = models.CharField(max_length=1, blank=True, choices=UserType.choices, default=UserType.user)
    api_key = models.CharField(max_length=50, null=True, blank=True)
    authenticator = models.ForeignKey(AuthenticationUser, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.user_type}'
