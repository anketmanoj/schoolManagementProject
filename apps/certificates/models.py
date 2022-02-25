from django.db import models
from apps.utils.models import Timestamps


class Certificates(Timestamps, models.Model):
    """
    Model for certificates
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
