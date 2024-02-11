from rest_framework.permissions import IsAuthenticated

from fabrique.articles.articles_views import BaseViewSet

from .models import (
    PhotoPrestataire,
    PhotoRepresentantPrestataire,
    Prestataire,
    RepresentantPrestataire,
)
from .serializers import *


class PrestataireViewSet(BaseViewSet):
    queryset = Prestataire.objects.all()
    serializer_class = PrestataireSerializer
    permission_classes = (IsAuthenticated,)


class RepresentantPrestataireViewSet(BaseViewSet):
    queryset = RepresentantPrestataire.objects.all()
    serializer_class = RepresentantPrestataireSerializer
    permission_classes = (IsAuthenticated,)


class PhotoPrestataireViewSet(BaseViewSet):
    queryset = PhotoPrestataire.objects.all()
    serializer_class = PhotoPrestataireSerializer
    permission_classes = (IsAuthenticated,)


class PhotoRepresentantPrestataireViewSet(BaseViewSet):
    queryset = PhotoRepresentantPrestataire.objects.all()
    serializer_class = PhotoRepresentantPrestataireSerializer
    permission_classes = (IsAuthenticated,)
