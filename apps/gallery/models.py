import time

from django.db import models

from apps.language.models import Language
from utils.abstract import AbstractModel


class Image(AbstractModel):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'image'
        ordering = ['id']


class ContentImage(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, related_name='image_content')
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    image_name = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=500)
    description = models.TextField()

    class Meta:
        db_table = 'content_image'
        ordering = ['id']
