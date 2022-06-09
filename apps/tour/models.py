import time

from django.db import models

from apps.gallery.models import Image
from apps.language.models import Language
from utils.abstract import AbstractModel


class TypeTour(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    type_name = models.CharField(max_length=255)

    class Meta:
        db_table = "type_tour"
        ordering = ['id']


class Tour(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    tour_name = models.CharField(max_length=255)

    tour_price = models.FloatField(null=True)
    tour_type = models.ForeignKey(TypeTour, on_delete=models.CASCADE, related_name='tour_type')

    tour_url = models.CharField(max_length=1000)
    tour_meta_keywords = models.CharField(max_length=500)

    tour_images = models.ManyToManyField(Image, db_table="tour_images")

    def __str__(self):
        return self.tour_name

    class Meta:
        db_table = "tour"
        ordering = ['id']


class ContentTour(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    tour_name = models.CharField(max_length=255)
    tour_info = models.TextField()

    class Meta:
        db_table = 'content_tour'
        ordering = ['id']
