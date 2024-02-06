import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

from ets_alexis.utils import DEFAULT_SIZE, get_uuid

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")

#         email = self.normalize_email(email)
#         user = self.model(email=email, username=username)

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(email, username, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     class Meta:
#         verbose_name = "User"

#     def save(self, *args, **kwargs):
#         self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.email
    

class User(AbstractUser):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)

    # when loggin in, we want to return the user's email instead of username
    USERNAME_FIELD = "email"
    # when creating a new user, we want to use the email field instead of username
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
