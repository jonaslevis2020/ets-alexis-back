from dataclasses import field

from ..articles.serializers import BaseSerializer

from fabrique.infrastructures.models import Outil, PhotoOutil


class OutilSerializer(BaseSerializer):
    class Meta:
        model = Outil
        fields = "__all__"
        read_only_fields = ['id', 'creation_date', 'last_modified', 'creator']

class PhotoOutilSerializer(BaseSerializer):
    class Meta:
        model = PhotoOutil
        fields = "__all__"
        read_only_fields = ['id', 'creation_date', 'last_modified', 'creator']