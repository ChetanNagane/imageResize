from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _
"""
name of fish, species, weight, length, latitude, longitude and a timestamp
"""

# Create your models here.
class record(models.Model):
    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64)
    weight = models.FloatField(max_length=16)
    length = models.FloatField(max_length=16)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    timestamp = models.TimeField(auto_now_add=True)
    image = models.ImageField(_("Image"),upload_to="images/", blank=True)
