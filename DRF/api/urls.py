from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from DRF.api.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from DRF.api import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]