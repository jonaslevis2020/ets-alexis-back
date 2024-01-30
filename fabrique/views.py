from rest_framework.views import APIView
from colorama import Fore, Style, init
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from fabrique.articles.models import Article, PhotoArticle, Variation

from .articles.serializers import (
    ArticleSerializer,
    ArticleVariationSerializer,
    PhotoArticleSerializer,
)

init(autoreset=True)

# This apllies the custom save method to all views
class BaseViewSet(viewsets.ModelViewSet):
    # set the creator to the current authenticated user
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
    

class ArticleViewSet(BaseViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class PhotoArticleViewSet(BaseViewSet):
    queryset = PhotoArticle.objects.all()
    serializer_class = PhotoArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)



class VariationViewSet(BaseViewSet):
    queryset = Variation.objects.all()
    serializer_class = ArticleVariationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GetAppsNamesView(APIView):
    def get(self, request):
        data = {"fabrique", "quincaillerie", "immobilier"}
        print(f"{Style.BRIGHT+Fore.YELLOW}{data}")
        return Response(data)
