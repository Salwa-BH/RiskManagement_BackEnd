from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path
router = DefaultRouter()

router.register('custom-users', views.CustomUserViewSet)
