from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.users.views import UserViewsSet, EmployeeAPIViews


router = DefaultRouter()
router.register('users', UserViewsSet, basename='api_users')
router.register('employee', EmployeeAPIViews, basename='api_employee')
 
urlpatterns=[
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('refresh/', TokenRefreshView.as_view(), name='api_refresh'),
]

urlpatterns += router.urls  