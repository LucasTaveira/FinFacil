from .models import AuthenticationUser, User
from rest_framework import serializers

class AuthenticationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticationUser
        fields = (
            'email',
            'password',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
