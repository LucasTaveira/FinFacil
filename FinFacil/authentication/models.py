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
        
