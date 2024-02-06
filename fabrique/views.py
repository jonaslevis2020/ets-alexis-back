from colorama import Fore, Style, init
from rest_framework.response import Response
from rest_framework.views import APIView

from .articles.articles_views import (ArticleViewSet, PhotoArticleViewSet,
                                      VariationViewSet)

from .infrastructures.ifrs_views import OutilViewSets, PhotoOutilViewSets

init(autoreset=True)


class GetAppsNamesView(APIView):
    def get(self, request):
        data = {"fabrique", "quincaillerie", "immobilier"}
        print(f"{Style.BRIGHT+Fore.YELLOW}{data}")
        return Response(data)
