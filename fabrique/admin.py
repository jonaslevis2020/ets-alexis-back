from django.contrib import admin
from fabrique.articles.models import Article, Variation, PhotoArticle
from fabrique.infrastructures.models import Outils
from fabrique.ressources_humaines.clients.models import Client, PhotoClient, PhotoRepresentantClient, RepresentantClient
from fabrique.ressources_humaines.personel.models import Employer, PhotoEmployer
from fabrique.ressources_humaines.prestataires.models import Prestataire, RepresentantPrestataire, PhotoPrestataire, PhotoRepresentantPrestataire

# Register your models here.

#Aritcles
admin.site.register(Article)
admin.site.register(PhotoArticle)
admin.site.register(Variation)

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
