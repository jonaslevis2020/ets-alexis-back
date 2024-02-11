from django.contrib import admin
from django.utils.html import format_html

from fabrique.articles.models import Article, PhotoArticle, Variation
from fabrique.infrastructures.models import Outil, PhotoOutil
from fabrique.ressources_humaines.clients.models import (
    Client,
    PhotoClient,
    PhotoRepresentantClient,
    RepresentantClient,
)
from fabrique.ressources_humaines.personel.models import Employer, PhotoEmployer
from fabrique.ressources_humaines.prestataires.models import (
    PhotoPrestataire,
    PhotoRepresentantPrestataire,
    Prestataire,
    RepresentantPrestataire,
)


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
    def image_thumbnail(self, obj: PhotoArticle):
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


# /////////////////////////////////////////////////////////////////////


# Infrastructures
@admin.register(Outil)
class OutilAdmin(BaseAdmin):
    # list_display = [field.name for field in Outil._meta.get_fields()]
    pass


@admin.register(PhotoOutil)
class PhotoOutilAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoOutil):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [field.name for field in PhotoOutil._meta.get_fields()] + [
        "image_thumbnail"
    ]


# /////////////////////////////////////////////////////////////////////


# Ressoureces Humaines
@admin.register(Client)
class ClientAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "address",
        "cni",
        "creator",
        "creation_date",
        "last_modified",
    ]


@admin.register(PhotoClient)
class ClientPhotoAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoClient):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [field.name for field in PhotoClient._meta.get_fields()] + [
        "image_thumbnail"
    ]


@admin.register(RepresentantClient)
class RepresentantClientAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "address",
        "cni",
        "creator",
        "creation_date",
        "last_modified",
    ]


@admin.register(PhotoRepresentantClient)
class PhotoRepresentantClientAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoRepresentantClient):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [
        field.name for field in PhotoRepresentantClient._meta.get_fields()
    ] + ["image_thumbnail"]


# /////////////////////////////////////////////////////////////////////


# Personnel
@admin.register(Employer)
class EmployerAdmin(BaseAdmin):
    list_display = [
        "id",
        "pseudo",
        "firstName",
        "lastName",
        "email",
        "phone",
        "address",
        "creator",
        "creation_date",
        "last_modified",
    ]
    list_display_links = [
        "id",
        "pseudo",
    ]


@admin.register(PhotoEmployer)
class EmployerPhotoAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoRepresentantClient):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [field.name for field in PhotoEmployer._meta.get_fields()] + [
        "image_thumbnail"
    ]


# /////////////////////////////////////////////////////////////////////


# Prestataire
@admin.register(Prestataire)
class PrestataireAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "siteWeb",
        "phone",
        "address",
        "role",
        "creator",
        "creation_date",
        "last_modified",
    ]
    list_display_links = [
        "id",
        "name",
    ]


@admin.register(PhotoPrestataire)
class PrestatairePhotoAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoPrestataire):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [field.name for field in PhotoPrestataire._meta.get_fields()] + [
        "image_thumbnail"
    ]


@admin.register(RepresentantPrestataire)
class RepresentantPrestataireAdmin(BaseAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone",
        "address",
        "cni",
        "creator",
        "creation_date",
        "last_modified",
    ]


@admin.register(PhotoRepresentantPrestataire)
class PhotoRepresentantPrestataireAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PhotoRepresentantPrestataire):
        return format_html(
            f'<img src="{obj.picture.url}" style="max-width:100px; max-height:100px"/>'
        )

    list_display = [
        field.name for field in PhotoRepresentantPrestataire._meta.get_fields()
    ] + ["image_thumbnail"]


# /////////////////////////////////////////////////////////////////////
