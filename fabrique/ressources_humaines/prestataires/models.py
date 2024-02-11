from tabnanny import verbose
from django.contrib.auth import get_user_model
from django.db import models

from ets_alexis.utils import DEFAULT_SIZE, get_uuid


ROLES = [
    ("Representant", "Representant"),
    ("Responsable", "Responsable"),
    ("Propriétaire", "Propriétaire"),
]


class Prestataire(models.Model):
    id = models.CharField(
        primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE, editable=False
    )
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
    id = models.CharField(
        primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE, editable=False
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(
        max_length=20,
    )
    address = models.CharField(max_length=50, blank=True)
    cni = models.CharField(max_length=50, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    prestataire = models.ForeignKey(
        Prestataire, related_name="representants", on_delete=models.CASCADE
    )

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class PhotoRepresentantPrestataire(models.Model):
    id = models.CharField(
        primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE, editable=False
    )
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

    class Meta:
        verbose_name = "Photos Représentants Prestataires"
    def get_representant_name(self):
        return self.representant.name

    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_representant_name()}/{self.picture.name}"
        print(f"****** {self.picture.name}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.representant.name


class PhotoPrestataire(models.Model):
    id = models.CharField(
        primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE, editable=False
    )
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/prestataires", blank=True)
    prestataire = models.ForeignKey(
        Prestataire, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Photos Prestataires"

    def get_prestataire_name(self):
        return self.prestataire.name

    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_prestataire_name()}/{self.picture.name}"
        print(f"****** {self.picture.name}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.prestataire.name
