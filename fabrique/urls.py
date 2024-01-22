from django.urls import path
from .views import UserCreate, UserDelete, UserList, UserRetrieve, UserUpdate

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserRetrieve.as_view()),
    path('create/', UserCreate.as_view()),
    path('update/<int:pk>/', UserUpdate.as_view()),
    path('delete/<int:pk>/', UserDelete.as_view()),
]
