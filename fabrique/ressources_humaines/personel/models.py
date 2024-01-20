from django.contrib.auth import get_user_model
from django.db import models


ROLES = [
    ("Gerant", "Gerant"),
    ("Fabricant", "Fabricant"),
    ("Chauffeur", "chauffeur"),
    ("Manutentionnaire", "Manutentionnaire"),
]


class Employer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50, blank=True)
    email = models.EmailField(("Adresse mail"), max_length=254, blank=True)
    phone = models.CharField(verbose_name="numero de telephone", max_length=20)
    address = models.CharField(max_length=50)
    role = models.CharField(choices=ROLES, max_length=50)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.firstName


class PhotoEmployer(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/Employers", blank=True)
    employer = models.ForeignKey(
        Employer, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk
