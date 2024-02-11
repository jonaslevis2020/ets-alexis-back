from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

fabrique_router = DefaultRouter()

# Articles
fabrique_router.register(r"articles", ArticleViewSet)
fabrique_router.register(r"photos_articles", PhotoArticleViewSet)
fabrique_router.register(r"variations", VariationViewSet)

# Infrastructures
fabrique_router.register(r"outils", OutilViewSets)
fabrique_router.register(r"photo_outils", PhotoOutilViewSets)

# Ressources Humaines
# **** Clients
fabrique_router.register(r"clients", ClientsViewSet)
fabrique_router.register(r"representants", RepresentantClientViewSets)
fabrique_router.register(r"photos_clients", PhotoClientViewSets)
fabrique_router.register(r"photos_representants", PhotoRepresentantClientViewSets)

# **** Personel
fabrique_router.register(r"employers", EmployersViewSet)
fabrique_router.register(r"photos_employers", PhotoEmployersViewSet)

# **** Prestataires
fabrique_router.register(r"prestataires", PrestataireViewSet)
fabrique_router.register(r"representants_prestataires", RepresentantPrestataireViewSet)
fabrique_router.register(r"photos_prestataires", PhotoPrestataireViewSet)
fabrique_router.register(r"photos_representants_prestataires", PhotoRepresentantPrestataireViewSet)

urlpatterns = [
    path("", include(fabrique_router.urls)),
    path("services/", GetAppsNamesView.as_view()),
]
