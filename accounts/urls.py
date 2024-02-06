from django.urls import include, path
from .views import ChangePasswordViewSet, LoginViewSet, LogoutViewSet
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserLogIn

accounts_router = DefaultRouter()
accounts_router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(accounts_router.urls)),
    path('login/', UserLogIn.as_view()),
    path('logout/', LogoutViewSet.as_view({'post': 'create'})),
]