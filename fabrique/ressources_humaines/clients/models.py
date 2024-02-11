from django.contrib.auth import get_user_model
from django.db import models
from ets_alexis.utils import DEFAULT_SIZE, get_uuid

import datetime


class Client(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.TextField(max_length=20)
    address = models.CharField(max_length=50, blank=True)
    cni = models.CharField(max_length=50, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class RepresentantClient(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.TextField(max_length=20)
    address = models.CharField(max_length=50, blank=True)
    cni = models.CharField(max_length=50, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    client = models.ForeignKey(
        Client, related_name="representants", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class PhotoRepresentantClient(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/clients/representants")
    representant = models.ForeignKey(
        RepresentantClient, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Photos Representants Clients"

    def get_representant_name(self):
        return self.representant.name

    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_representant_name()}/{self.picture.name}"
        print(f"****** {self.picture.name}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.representant.name


class PhotoClient(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/clients")
    client = models.ForeignKey(Client, related_name="photos", on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Photos Clients"

    def get_client_name(self):
        return self.client.name

    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_client_name()}/{self.picture.name}"
        print(f"****** {self.picture.name}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.client.name
