from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fabrique.infrastructures.ifrs_views import OutilViewSets, PhotoOutilViewSets

from .views import (
    ArticleViewSet,
    PhotoArticleViewSet,
    VariationViewSet,
    GetAppsNamesView,
)

fabrique_router = DefaultRouter()
fabrique_router.register(r"articles", ArticleViewSet)
fabrique_router.register(r"photos_articles", PhotoArticleViewSet)
fabrique_router.register(r"variations", VariationViewSet)
fabrique_router.register(r"outils", OutilViewSets)
fabrique_router.register(r"photo_outils", PhotoOutilViewSets)

urlpatterns = [
    path("", include(fabrique_router.urls)),
    path("services/", GetAppsNamesView.as_view()),
]
