from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from fabrique.infrastructures.models import Outil, PhotoOutil
from fabrique.infrastructures.serializers import OutilSerializer, PhotoOutilSerializer
from fabrique.articles.articles_views import BaseViewSet


class OutilViewSets(BaseViewSet):
    queryset = Outil.objects.all()
    serializer_class = OutilSerializer
    permission_classes = [IsAuthenticated]
    
class PhotoOutilViewSets(BaseViewSet):
    queryset = PhotoOutil.objects.all()
    serializer_class = PhotoOutilSerializer
    permission_classes = [IsAuthenticated]