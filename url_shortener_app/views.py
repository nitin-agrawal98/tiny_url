from datetime import datetime

from django.shortcuts import redirect
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from url_shortener_app.models import URLShortener
from url_shortener_app.serializers import URLShortenerSerializer
from url_shortener_app.utils import get_pk_id_from_base62_string


class URLShortenerViewSet(viewsets.ModelViewSet):
    serializer_class = URLShortenerSerializer

    def create(self, request, *args, **kwargs):
        queryset = URLShortener.objects.filter(original_url=request.data['original_url'],
                                               expiry_date__gte=datetime.now())
        if queryset.exists():
            serializer = URLShortenerSerializer(queryset.get())
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = URLShortenerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return URLShortener.objects.filter(expiry_date__gte=datetime.now())


@api_view(['GET'])
def get_original_url_from_short_url(request, short_url):
    pk = get_pk_id_from_base62_string(short_url)
    try:
        url_shortener = URLShortener.objects.get(pk=pk, expiry_date__gte=datetime.now())
    except URLShortener.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = URLShortenerSerializer(url_shortener)
    return redirect(serializer.data['original_url'])
