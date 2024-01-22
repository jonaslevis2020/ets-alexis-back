"""
URL configuration for ets_alexis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
import fabrique.urls as fabrique_urls
import fabrique.views as fabrique_views

router = DefaultRouter()
router.register(r"users", fabrique_views.UserViewSet, basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', fabrique_views.get_apps_names),
    path('', include(router.urls)),
    # path('users/', include(fabrique_urls)),
]
