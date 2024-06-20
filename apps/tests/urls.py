from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tests.views import TestViewSet

router = DefaultRouter()
router.register('tests', TestViewSet, basename='api_test')

urlpatterns = [
    
]

urlpatterns += router.urls