from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Article, PhotoArticle, Variation


class UserSerializer(serializers.ModelSerializer):
  # The password field is readonly
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ["id","username", "email", "password", "first_name", "last_name"]
        read_only_fields = ['password']

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class PhotoArticleSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    creator = UserSerializer()

    class Meta:
        model = PhotoArticle
        fields = ["description", "picture", "creation_date", "last_modified"]


class ArticleVariationSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    creator = UserSerializer()

    class Meta:
        model = Variation
        fields = [
            "variation_category",
            "variation_value",
            "is_active",
            "creation_date",
            "last_modified",
        ]
