from django.apps import apps
from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .articles.serializers import ChangePasswordSerializer, UserSerializer

from colorama import Style, Fore, init

init(autoreset=True)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreate(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=["GET"])
    def show_password(self, request: HttpRequest, pk=None):
        user: User = self.get_object()
        return Response(user.password)
      
    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user: User = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            new_password = serializer.data.get("new_password")

            if not user.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(new_password)
            user.save()

            return Response({'status': 'Password changed successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["GET"])
    def is_admin(self, request: HttpRequest, pk=None):
        user: User = self.get_object()
        return Response({"is_admin": user.is_superuser})

    @action(detail=True, methods=["GET"])
    def is_staff(self, request: HttpRequest, pk=None):
        user: User = self.get_object()
        return Response({"is_staff": user.is_staff})

    @action(detail=True, methods=["GET"])
    def is_active(self, request: HttpRequest, pk=None):
        user: User = self.get_object()
        return Response({"is_active": user.is_active})

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset
    
@api_view(['GET'])
def get_apps_names(request: HttpRequest):
    data = [app.name for app in apps.get_app_configs() if app.name in {'fabrique', 'quincaillerie', 'immobilier'}]
    print(f'{Style.BRIGHT+Fore.YELLOW}{data}')
    return Response(data)
