"""
    Views to handle user related operations.
"""
from rest_framework.mixins import CreateModelMixin

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from users.serializers import (UserSignupSerializer, UserSerializer,
                                        LoginSerializer)

class Signup(CreateModelMixin, viewsets.GenericViewSet):
    """Class to handle user signup"""
    serializer_class = UserSignupSerializer
    def create(self, request):
        data = request.data
        serializer = UserSignupSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        serializer = UserSerializer(user_obj)
        token = Token.objects.create(user=user_obj)
        data = serializer.data
        data.update({"token":token.key})
        return Response(data=data, status=200)

class Login(CreateModelMixin, viewsets.GenericViewSet):
    """View to login user and return their token"""
    serializer_class = LoginSerializer
    def create(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token, _ = Token.objects.get_or_create(user=serializer.validated_data.get('user'))
        serializer = UserSerializer(serializer.validated_data.get('user'))
        data = serializer.data
        data.update({"token":token.key})
        return Response(data=data, status=200)