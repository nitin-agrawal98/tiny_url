from django.urls import path, include
from rest_framework.routers import DefaultRouter

from url_shortener.settings import REDIRECT_URL
from . import views

router = DefaultRouter()
router.register(r'shortened-url', views.URLShortenerViewSet, basename='shortened-url')

urlpatterns = [
    path('', include(router.urls)),
    path(REDIRECT_URL + '<str:short_url>/', views.get_original_url_from_short_url,
         name='original_url_from_short_url')
]
