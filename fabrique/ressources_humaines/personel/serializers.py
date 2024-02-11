from .models import Employer, PhotoEmployer
from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    

class EmployerSerializer(BaseSerializer):
    class Meta:
        model = Employer
        fields = "__all__"


class PhotoEmployerSerializer(BaseSerializer):
    class Meta:
        model = PhotoEmployer
        fields = "__all__"
