from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Outils(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    

    creator = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title


class PhotoOutils(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/outils", blank=True)
    representant = models.ForeignKey(
        Outils, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk
    
    

