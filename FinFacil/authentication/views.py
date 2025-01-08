from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import AuthenticationUser, User
from .serializers import AuthenticationUserSerializer, UserSerializer

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

class UserViewSet(viewsets.ModelViewSet):
    """
    ### Description:
        This model should be used to create a user
        
    ### Fields:
        - first_name: The first name of the user
        - last_name: The last name of the user (optional)
        - whatsApp: phone number (optional)
        - user_type: USER or API (API is for who whant to use this API)
        
    ### Methods:
        - POST
        - GET
        - PUT
        - DELETE
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
