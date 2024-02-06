from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.forms import PasswordInput

from django.contrib.auth import get_user_model


class AuthenticationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    # The password field is readonly
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "password"]

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    # The password field is readonly
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "password"]
        read_only_fields = ("password",)

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
