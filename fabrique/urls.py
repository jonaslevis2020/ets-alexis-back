from django.urls import include, path
from rest_framework.routers import DefaultRouter

from fabrique.infrastructures.ifrs_views import (OutilViewSets,
                                                 PhotoOutilViewSets)

from .views import *

fabrique_router = DefaultRouter()

fabrique_router.register(r"articles", ArticleViewSet)
fabrique_router.register(r"photos_articles", PhotoArticleViewSet)
fabrique_router.register(r"variations", VariationViewSet)

fabrique_router.register(r"outils", OutilViewSets)
fabrique_router.register(r"photo_outils", PhotoOutilViewSets)

fabrique_router.register(r"clients", ClientsViewSet)
fabrique_router.register(r"representants", RepresentantClientViewSets)
fabrique_router.register(r"photos_clients", PhotoClientViewSets)
fabrique_router.register(r"photos_representants", PhotoRepresentantClientViewSets)

urlpatterns = [
    path("", include(fabrique_router.urls)),
    path("services/", GetAppsNamesView.as_view()),
]
