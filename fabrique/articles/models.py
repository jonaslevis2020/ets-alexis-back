import uuid

from django.contrib.auth import get_user_model
from django.db import models

from ets_alexis.utils import DEFAULT_SIZE, get_uuid


class Article(models.Model):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    title = models.CharField(max_length=50, verbose_name="Titre/Intitule/Nom", unique=True,)
    description = models.TextField(blank=True,  verbose_name="Description",)
    creation_date = models.DateField(auto_now_add=True, verbose_name="Date de Creation")
    last_modified = models.DateField(auto_now=True, verbose_name="Derniere Modification")

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name="Autheur")

    def __str__(self) -> str:
        return self.title


class PhotoArticle(models.Model):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    description = models.TextField(blank=True, max_length=250,  verbose_name="Decription", )
    picture = models.ImageField(upload_to="photos/Articles/", blank=True, verbose_name="Image/Photo")
    creation_date = models.DateField(auto_now_add=True, verbose_name="Date de creation")
    last_modified = models.DateField(auto_now=True, verbose_name="Derniere modification")

    article = models.ForeignKey(
        Article, related_name="photos", on_delete=models.CASCADE,
        verbose_name="Choix de l'article"
    )
    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, verbose_name="Auteur")
    
    class Meta:
        verbose_name = "Photos Articles"
    
    def get_article_name(self):
        return self.article.title 
    
    def save(self, *args, **kwargs):
        self.picture.name = f"{self.get_article_name()}/{self.picture.name}"
        print(f'****** {self.picture.name}')
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.article.title


class VariationManager(models.Manager):
    def longueur(self):
        return super(VariationManager, self).filter(
            variation_category="longueur", is_active=True
        )

    def largeur(self):
        return super(VariationManager, self).filter(
            variation_category="largeur", is_active=True
        )

    def diametre(self):
        return super(VariationManager, self).filter(
            variation_category="diametre", is_active=True
        )

    def forme(self):
        return super(VariationManager, self).filter(
            variation_category="forme", is_active=True
        )


class Variation(models.Model):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="variations"
    )
    variation_category = models.CharField(
        max_length=50,
        choices=(
            ("longueur", "longueur"),
            ("largeur", "largeur"),
            ("diametre", "diametre"),
            ("forme", "forme"),
        ),
        verbose_name="Type de variation"
    )
    description = models.TextField(blank=True, max_length=250,  verbose_name="Description", )
    variation_value = models.CharField(max_length=50,  verbose_name="Valeur de la variation")
    stock = models.IntegerField(verbose_name="Quantite en Stock", default=0)
    price = models.IntegerField(verbose_name="Prix Unitaire(en FCFA)", default=0)
    is_active = models.BooleanField(default=True,  verbose_name="Est actif")
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True,  verbose_name="Derniere modification")

    objects = VariationManager()

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True,  verbose_name="Auteur")

    def __str__(self):
        return self.variation_value
