from rest_framework.permissions import IsAuthenticated
from fabrique.articles.articles_views import BaseViewSet

from .models import Employer, PhotoEmployer
from .serializers import EmployerSerializer, PhotoEmployerSerializer


class EmployersViewSet(BaseViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = (IsAuthenticated,)


class PhotoEmployersViewSet(BaseViewSet):
    queryset = PhotoEmployer.objects.all()
    serializer_class = PhotoEmployerSerializer
    permission_classes = (IsAuthenticated,)
