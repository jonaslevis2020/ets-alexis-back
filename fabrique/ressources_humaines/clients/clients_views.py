from rest_framework.permissions import IsAuthenticated

from ...articles.articles_views import BaseViewSet
from .models import Client, PhotoClient, PhotoRepresentantClient, RepresentantClient
from .serializers import (
    ClientSerializer,
    PhotoClientSerializer,
    PhotoRepresentantClientSerializer,
    RepresentantClientSerializer,
)


class ClientsViewSet(BaseViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)


class RepresentantClientViewSets(BaseViewSet):
    queryset = RepresentantClient.objects.all()
    serializer_class = RepresentantClientSerializer
    permission_classes = (IsAuthenticated,)


class PhotoClientViewSets(BaseViewSet):
    queryset = PhotoClient.objects.all()
    serializer_class = PhotoClientSerializer
    permission_classes = (IsAuthenticated,)


class PhotoRepresentantClientViewSets(BaseViewSet):
    queryset = PhotoRepresentantClient.objects.all()
    serializer_class = PhotoRepresentantClientSerializer
    permission_classes = (IsAuthenticated,)
