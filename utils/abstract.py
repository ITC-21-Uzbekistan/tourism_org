from django.db import models

from apps.auth_user.models import User


class AbstractModel(models.Model):
    is_delete = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
