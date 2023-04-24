from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CustomUserSerializer 
from .models import CustomUser

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('last_name')
    serializer_class = CustomUserSerializer
    search_fields = ('email')
    ordering_fields = ('last_name')
    readonly_fields = ('date_joined','last_login')

