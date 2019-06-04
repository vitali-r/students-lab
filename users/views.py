from django.shortcuts import render
from  django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import viewsets, generics, permissions

class RegistrationView(generics.CreateAPIView):
    user_model = get_user_model()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

