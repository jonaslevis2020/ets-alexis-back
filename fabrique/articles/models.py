from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title


class PhotoArticle(models.Model):
    description = models.TextField(blank=True, max_length=250)
    picture = models.ImageField(upload_to="photos/Articles", blank=True)
    article = models.ForeignKey(
        Article, related_name="photos", on_delete=models.CASCADE
    )
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.pk


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
    )
    variation_value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    objects = VariationManager()

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.variation_value
