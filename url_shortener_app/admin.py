from django.contrib import admin

# Register your models here.
from url_shortener_app.models import URLShortener


class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'shortened_url', 'created_date', 'expiry_date')


admin.site.register(URLShortener, URLShortenerAdmin)
