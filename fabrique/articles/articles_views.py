from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Article, PhotoArticle, Variation
from .serializers import (ArticleSerializer, ArticleVariationSerializer,
                          PhotoArticleSerializer)


# This apllies the custom save method to all views
class BaseViewSet(viewsets.ModelViewSet):
    # set the creator to the current authenticated user
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ArticleViewSet(BaseViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class PhotoArticleViewSet(BaseViewSet):
    queryset = PhotoArticle.objects.all()
    serializer_class = PhotoArticleSerializer
    permission_classes = (IsAuthenticated,)


class VariationViewSet(BaseViewSet):
    queryset = Variation.objects.all()
    serializer_class = ArticleVariationSerializer
    permission_classes = (IsAuthenticated,)
