import time

from django.db import models


class Language(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True, default=int(time.time() * 10), unique=True)
    language_name = models.CharField(max_length=255)
    language_short = models.CharField(max_length=10)

    def __str__(self):
        return self.language_name

    class Meta:
        ordering = ['id']
