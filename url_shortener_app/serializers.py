from rest_framework import serializers

from url_shortener_app.models import URLShortener


class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortener
        fields = ['shortened_url', 'original_url']
