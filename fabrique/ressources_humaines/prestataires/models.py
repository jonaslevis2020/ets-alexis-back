from django.contrib.auth import get_user_model
from django.db import models


ROLES = [("Representant", "Representant"), ("Responsable", "Responsable")]


class Prestataire(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    siteWeb = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=ROLES, max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class RepresentantPrestataire(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.TextField(max_length=20, blank=True)
    address = models.CharField(max_length=50)
    cni = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    prestataire = models.ForeignKey(
        Prestataire, related_name="representants", on_delete=models.CASCADE
    )

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class PhotoRepresentantPrestataire(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(
        upload_to="photos/prestataires/representants", blank=True
    )
    representant = models.ForeignKey(
        RepresentantPrestataire, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk


class PhotoPrestataire(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/prestataires", blank=True)
    representant = models.ForeignKey(
        Prestataire, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk
