from .models import AuthenticationUser
from rest_framework import serializers

class AuthenticationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticationUser
        fields = (
            'email',
            'password',
        )
