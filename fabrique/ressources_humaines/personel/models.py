from tabnanny import verbose
from django.contrib.auth import get_user_model
from django.db import models

from ets_alexis.utils import DEFAULT_SIZE, get_uuid


ROLES = [
    ("Gerant", "Gerant"),
    ("Fabricant", "Fabricant"),
    ("Chauffeur", "chauffeur"),
    ("Manutentionnaire", "Manutentionnaire"),
]


class Employer(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    pseudo = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50, blank=True)
    lastName = models.CharField(max_length=50, blank=True)
    email = models.EmailField(("Adresse mail"), max_length=254, blank=True)
    phone = models.CharField(verbose_name="numero de telephone", max_length=20)
    address = models.CharField(max_length=50, blank=True)
    role = models.CharField(choices=ROLES, max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pseudo


class PhotoEmployer(models.Model):
    id = models.CharField(
        primary_key=True, max_length=DEFAULT_SIZE, default=get_uuid, editable=False
    )
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/Employers", blank=True)
    employer = models.ForeignKey(
        Employer, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Photos Employers"

    def get_employer_name(self):
        return self.employer.pseudo

    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_employer_name()}/{self.picture.name}"
        print(f"****** {self.picture.name}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.employer.pseudo
