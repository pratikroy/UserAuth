from rest_framework import generics

from user.serializers import UserSerializer
from user.serializers import UserLoginSerializer

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser

from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)




class ListUserView(generics.ListAPIView):
    """Create new queryset for all users"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)




class UserManageView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Destroy a single user record"""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    lookup_field = 'email'




class UserLoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token': serializer.data['token']
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


