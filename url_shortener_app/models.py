import datetime

from django.db import models

from url_shortener.settings import BASE_URL, REDIRECT_URL
from url_shortener_app.utils import get_base62_string_from_id


# Create your models here.
class URLShortener(models.Model):
    original_url = models.CharField(max_length=2048)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    expiry_date = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        self.expiry_date = datetime.datetime.now() + datetime.timedelta(hours=12)
        super(URLShortener, self).save(*args, **kwargs)

    @property
    def shortened_url(self):
        encoded_string = ''
        if self.id:
            encoded_string = get_base62_string_from_id(self.id)
        return BASE_URL + REDIRECT_URL + encoded_string if encoded_string is not None else None

    def __str__(self):
        return self.original_url
