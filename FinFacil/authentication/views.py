from django.shortcuts import render

from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny

from .models import AuthenticationUser
from .serializers import AuthenticationUserSerializer

class AuthenticationUserView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    """
    ### Description:
        This model should be used to create a authenticator to users
        
    ### Fields:
        - email: The email of the user
        - password: The password of the user
        
    ### Methods:
        - POST
    """
    
    queryset = AuthenticationUser.objects.all()
    serializer_class = AuthenticationUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

