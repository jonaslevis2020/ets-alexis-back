from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Article, PhotoArticle, Variation


class BaseSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(read_only=True)
    # set the creator field as read_only
    creator = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    

class ArticleSerializer(BaseSerializer):

    class Meta:
        model = Article
        fields = "__all__"


class PhotoArticleSerializer(BaseSerializer):
    """
    Serializer for the PhotoArticle model.

    Fields:
    - description (str): The description of the photo article.
    - article (ArticleSerializer): The serialized representation of the associated article.
    - creator (PrimaryKeyRelatedField): The primary key of the creator of the photo article.
    - picture (ImageField): The picture of the photo article.
    - creation_date (DateTimeField): The date and time of creation of the photo article.
    - last_modified (DateTimeField): The date and time of the last modification of the photo article.

    Methods:
    - create(validated_data): Creates a new PhotoArticle instance with the provided validated data.

    Args:
        validated_data (dict): The validated data for creating the PhotoArticle instance.

    Returns:
        PhotoArticle: The created PhotoArticle instance."""

    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all(), read_only=False)

    class Meta:
        model = PhotoArticle
        fields = "__all__"

    # def create(self, validated_data):
    #     """
    #     Creates a new PhotoArticle instance with the provided validated data.

    #     Args:
    #         validated_data (dict): The validated data for creating the PhotoArticle instance.

    #     Returns:
    #         PhotoArticle: The created PhotoArticle instance."""

    #     article_data = validated_data.pop("article")
    #     article = Article.objects.create(**article_data)
    #     return PhotoArticle.objects.create(article=article, **validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Updates an existing instance with the provided validated data.

    #     Args:
    #         instance: The existing instance to be updated.
    #         validated_data (dict): The validated data for updating the instance.

    #     Returns:
    #         The updated instance."""

    #     article_data = validated_data.pop("article")
    #     article = instance.article
    #     for attr, value in article_data.items():
    #         setattr(article, attr, value)
    #     article.save()

    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()

    #     return instance


class ArticleVariationSerializer(BaseSerializer):
    article = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())

    class Meta:
        model = Variation
        fields = [
            "id",
            "variation_category",
            "variation_value",
            "article",
            "creator",
            "is_active",
            "creation_date",
            "last_modified",
        ]
        read_only_fields = ["creator"]

    # def create(self, validated_data):
    #     """
    #     Create a new Variation instance.

    #     Args:
    #         validated_data (dict): The validated data for creating the Variation instance.

    #     Returns:
    #         Variation: The newly created Variation instance.
    #     """
    #     article_data = validated_data.pop("article")
    #     article = Article.objects.create(**article_data)
    #     return Variation.objects.create(article=article, **validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update an existing Variation instance.

    #     Args:
    #         instance (Variation): The Variation instance to be updated.
    #         validated_data (dict): The validated data for updating the Variation instance.

    #     Returns:
    #         Variation: The updated Variation instance."""

    #     article_data = validated_data.pop("article")
    #     article = instance.article
    #     for attr, value in article_data.items():
    #         setattr(article, attr, value)
    #     article.save()

    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()

    #     return instance
