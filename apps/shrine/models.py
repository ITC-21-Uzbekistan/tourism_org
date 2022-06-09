import time

from django.db import models

from apps.country.models import Country
from apps.gallery.models import Image
from apps.language.models import Language
from apps.region.models import Region
from utils.abstract import AbstractModel


class Shrine(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    shrine_name = models.CharField(max_length=255)
    shrine_url = models.CharField(max_length=1000)
    shrine_meta_keywords = models.TextField()

    shrine_location_longitude = models.FloatField()
    shrine_location_latitude = models.FloatField()

    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    shrine_images = models.ManyToManyField(Image, db_table="shrine_images", related_name='shrine_images')

    class Meta:
        db_table = 'shrine'
        ordering = ['id']

    def __str__(self):
        return self.shrine_name


class ContentShrine(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    shrine = models.ForeignKey(Shrine, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    shrine_name = models.CharField(max_length=255)
    shrine_info = models.TextField()

    class Meta:
        db_table = 'content_shrine'
        ordering = ['id']
