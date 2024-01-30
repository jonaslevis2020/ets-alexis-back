from django.contrib import admin
from fabrique.articles.models import Article, Variation, PhotoArticle
from fabrique.infrastructures.models import Outils
from fabrique.ressources_humaines.clients.models import Client, PhotoClient, PhotoRepresentantClient, RepresentantClient
from fabrique.ressources_humaines.personel.models import Employer, PhotoEmployer
from fabrique.ressources_humaines.prestataires.models import Prestataire, RepresentantPrestataire, PhotoPrestataire, PhotoRepresentantPrestataire



class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('creator',)
    # set the creator to the current authenticated user
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

#Aritcles
@admin.register(Article)
class ArticleAdmin(BaseAdmin):
    list_display = ('id','title', 'description', 'creator', 'creation_date', 'last_modified')
    list_display_links = ('id','title', 'creator')
    
        
@admin.register(PhotoArticle)
class PhotoArticleAdmin(BaseAdmin):
    pass

@admin.register(Variation)
class VariationAdmin(BaseAdmin):
    list_display = ('variation_category', 'variation_value', 'article', 'description', 'stock', 'price')

#Infrastructures
admin.site.register(Outils)

#Ressoureces Humaines
admin.site.register(Client)
admin.site.register(RepresentantClient)
admin.site.register(PhotoClient)
admin.site.register(PhotoRepresentantClient)
admin.site.register(Employer)
admin.site.register(PhotoEmployer)

#Prestataire
admin.site.register(Prestataire)
admin.site.register(RepresentantPrestataire)
admin.site.register(PhotoRepresentantPrestataire)
admin.site.register(PhotoPrestataire)
