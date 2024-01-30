from django.contrib.auth import (authenticate, get_user_model, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpRequest
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import AuthenticationSerializer, ChangePasswordSerializer, UserSerializer


class UserLogIn(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username
        })


class AuthViewSet(viewsets.ModelViewSet):
    
    serializer_class = AuthenticationSerializer
    permission_classes = [AllowAny]
    

    def login(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Login Successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

    def logout(self, request):
        logout(request)
        return Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)

    def change_password(self, request):
        form = PasswordChangeForm(request.user, request.data)
        if not form.is_valid():
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        user = form.save()
        update_session_auth_hash(request, user) # Important!
        return Response({"detail": "Password Change Successful"}, status=status.HTTP_200_OK)

class LoginViewSet(AuthViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        return self.login(request)

class LogoutViewSet(AuthViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        return self.logout(request)

class ChangePasswordViewSet(AuthViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        return self.change_password(request)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["GET"])
    def show_password(self, request: HttpRequest, pk=None):
        user: get_user_model() = self.get_object()
        return Response(user.password)

    @action(detail=True, methods=["post"])
    def change_password(self, request, pk=None):
        user: get_user_model() = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not user.check_password(old_password):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(new_password)
            user.save()

            return Response(
                {"status": "Password changed successfully"}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"])
    def is_admin(self, request: HttpRequest, pk=None):
        user: get_user_model() = self.get_object()
        return Response({"is_admin": user.is_superuser})

    @action(detail=True, methods=["GET"])
    def is_staff(self, request: HttpRequest, pk=None):
        user: get_user_model() = self.get_object()
        return Response({"is_staff": user.is_staff})

    @action(detail=True, methods=["GET"])
    def is_active(self, request: HttpRequest, pk=None):
        user: get_user_model() = self.get_object()
        return Response({"is_active": user.is_active})

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
