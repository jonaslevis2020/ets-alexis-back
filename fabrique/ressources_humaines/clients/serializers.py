from rest_framework import serializers
from .models import Client, RepresentantClient, PhotoRepresentantClient, PhotoClient


class BaseSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    

class ClientSerializer(BaseSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class PhotoClientSerializer(BaseSerializer):
    class Meta:
        model = PhotoClient
        fields = "__all__"


class RepresentantClientSerializer(BaseSerializer):
    class Meta:
        model = RepresentantClient
        fields = "__all__"


class PhotoRepresentantClientSerializer(BaseSerializer):
    class Meta:
        model = PhotoRepresentantClient
        fields = "__all__"
