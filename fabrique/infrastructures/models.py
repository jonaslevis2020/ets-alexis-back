from django.contrib.auth import get_user_model
from django.db import models

from ets_alexis.utils import DEFAULT_SIZE, get_uuid


class Outil(models.Model):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
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


class PhotoOutil(models.Model):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/Outils", blank=True)
    representant = models.ForeignKey(
        Outil, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk
