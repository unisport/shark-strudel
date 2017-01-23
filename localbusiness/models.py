from __future__ import unicode_literals

from django.db import models


class LocalBusiness(models.Model):
    name = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=255, null=True)
    addressLocality = models.CharField(max_length=100, null=True)
    addressRegion = models.CharField(max_length=100, null=True)
    addressCountry = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=100, null=True)


class OpeningHours(models.Model):
    localbusiness = models.ForeignKey(LocalBusiness, on_delete=models.CASCADE)
    openinghours = models.CharField(max_length=255)
    display_order = models.IntegerField(default=0)
