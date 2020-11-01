from rest_framework import generics

from user.serializers import UserSerializer

from django.contrib.auth import get_user_model



class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer




class ListUserView(generics.ListAPIView):
    """Create new queryset for all users"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
