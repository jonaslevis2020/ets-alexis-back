from rest_framework import serializers
from .models import (
    Prestataire,
    RepresentantPrestataire,
    PhotoPrestataire,
    PhotoRepresentantPrestataire,
)


class BaseSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(read_only=True)


class PrestataireSerializer(BaseSerializer):
    class Meta:
        model = Prestataire
        fields = "__all__"


class RepresentantPrestataireSerializer(BaseSerializer):
    class Meta:
        model = RepresentantPrestataire
        fields = "__all__"


class PhotoPrestataireSerializer(BaseSerializer):
    class Meta:
        model = PhotoPrestataire
        fields = "__all__"


class PhotoRepresentantPrestataireSerializer(BaseSerializer):
    class Meta:
        model = PhotoRepresentantPrestataire
        fields = "__all__"
