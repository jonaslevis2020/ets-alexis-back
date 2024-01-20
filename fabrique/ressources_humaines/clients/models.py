from django.contrib.auth import get_user_model
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    address = models.CharField(max_length=50)
    cni = models.CharField(max_length=50)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class RepresentantClient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    address = models.CharField(max_length=50)
    cni = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    client = models.ForeignKey(
        Client, related_name="representants", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class PhotoRepresentantClient(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/clients/representants", blank=True)
    representant = models.ForeignKey(
        RepresentantClient, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk


class PhotoClient(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/clients", blank=True)
    representant = models.ForeignKey(
        Client, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk
