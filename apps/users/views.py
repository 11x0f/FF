from rest_framework import generics, permissions
from .serializers import RegisterSerializer, UserSerializer, PublicUserSerializer
from django.shortcuts import get_object_or_404
from .models import User

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class PublicProfileView(generics.RetrieveAPIView):
    serializer_class = PublicUserSerializer
    permission_classes = [permissions.AllowAny]
    def get_object(self):
        return get_object_or_404(User, alias = self.kwargs['alias'])
