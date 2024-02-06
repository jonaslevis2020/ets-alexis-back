from django.contrib import admin
from fabrique.articles.models import Article, Variation, PhotoArticle
from fabrique.infrastructures.models import Outil, PhotoOutil
from fabrique.ressources_humaines.clients.models import Client, PhotoClient, PhotoRepresentantClient, RepresentantClient
from fabrique.ressources_humaines.personel.models import Employer, PhotoEmployer
from fabrique.ressources_humaines.prestataires.models import (
    Prestataire,
    RepresentantPrestataire,
    PhotoPrestataire,
    PhotoRepresentantPrestataire,
)
from django.utils.html import format_html


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("creator",)

    # set the creator to the current authenticated user
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


# Aritcles
@admin.register(Article)
class ArticleAdmin(BaseAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "creator",
        "creation_date",
        "last_modified",
    )
    list_display_links = ("id", "title", "creator")


@admin.register(PhotoArticle)
class PhotoArticleAdmin(BaseAdmin):
    def image_thumbnail(self, obj:PhotoArticle):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )
    list_display = [field.name for field in PhotoArticle._meta.get_fields()] + [
        "image_thumbnail"
    ]


@admin.register(Variation)
class VariationAdmin(BaseAdmin):
    list_display = (
        "variation_category",
        "variation_value",
        "article",
        "description",
        "stock",
        "price",
    )


# Infrastructures
@admin.register(Outil)
class OutilAdmin(BaseAdmin):
    # list_display = [field.name for field in Outil._meta.get_fields()]
    pass
    


@admin.register(PhotoOutil)
class PhotoOutilAdmin(BaseAdmin):
    def image_thumbnail(self, obj:PhotoOutil):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [field.name for field in PhotoOutil._meta.get_fields()] + [
        "image_thumbnail"
    ]


# Ressoureces Humaines
admin.site.register(Client)
admin.site.register(RepresentantClient)
admin.site.register(PhotoClient)
admin.site.register(PhotoRepresentantClient)
admin.site.register(Employer)
admin.site.register(PhotoEmployer)

# Prestataire
admin.site.register(Prestataire)
admin.site.register(RepresentantPrestataire)
admin.site.register(PhotoRepresentantPrestataire)
admin.site.register(PhotoPrestataire)
