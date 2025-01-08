from rest_framework import mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from .models import AuthenticationUser, User
from .serializers import AuthenticationUserSerializer, UserSerializer

class AuthenticationUserView(
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
   
    queryset = AuthenticationUser.objects.all()
    serializer_class = AuthenticationUserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    def get_queryset(self):
        try:
            if self.request.user.is_authenticated:
                return User.objects.filter(authenticator=self.request.user)
        except User.DoesNotExist:
            return super().get_queryset()
