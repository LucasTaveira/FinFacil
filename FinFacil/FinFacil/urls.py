"""
URL configuration for FinFacil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from rest_framework import routers

from control.views.income_view import UserIncomeItensView, UserIncomeView
from control.views.spending_plan_view import SpendingPlanItensView, SpendingPlanView
from authentication.views import AuthenticationUserView, UserViewSet
from control.views.monthly_expense_view import MonthlyExpenseItensView, MonthlyExpenseView

schema_view = get_schema_view(
    openapi.Info(
        title="FinFacil API",
        default_version='v1',
        description="API para FinFacil",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lucastaveira.lt@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'user/income', UserIncomeView, basename='user-income')
router.register(r'user/income-itens', UserIncomeItensView, basename='user-income-itens')
router.register(r'spending-plan', SpendingPlanView, basename='spending-plan')
router.register(r'spending-plan-itens', SpendingPlanItensView, basename='spending-plan-itens')
router.register(r'monthly-expense', MonthlyExpenseView, basename='monthly-expense')
router.register(r'monthly-expense-itens', MonthlyExpenseItensView, basename='monthly-expense-itens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('api/v1/',include(router.urls)),
    
    path('api/v1/signup/', AuthenticationUserView.as_view(), name='sign_up'),
]
