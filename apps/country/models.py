import time
from apps.gallery.models import Image
from apps.language.models import Language
from utils.abstract import AbstractModel
from django.db import models


class Country(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    country_name = models.CharField(max_length=255)
    country_url = models.CharField(max_length=255)
    country_meta_keywords = models.CharField(max_length=500)

    country_images = models.ManyToManyField(Image, db_table='country_images', related_name='country_images')

    class Meta:
        db_table = 'country'
        ordering = ['id']


class ContentCountry(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=255)
    country_info = models.TextField()

    class Meta:
        db_table = 'content_country'
        ordering = ['id']
