import time
from django.db import models
from apps.country.models import Country
from apps.gallery.models import Image
from apps.language.models import Language
from utils.abstract import AbstractModel


class Region(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    region_name = models.CharField(max_length=255)
    region_url = models.CharField(max_length=255)
    region_meta_keywords = models.CharField(max_length=500)

    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    region_images = models.ManyToManyField(Image, db_table='region_images', related_name='region_images')

    class Meta:
        db_table = 'region'
        ordering = ['id']

    def __str__(self):
        return self.region_name


class ContentRegion(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    region_name = models.CharField(max_length=255)
    region_info = models.TextField()

    class Meta:
        db_table = 'content_region'
        ordering = ['id']

