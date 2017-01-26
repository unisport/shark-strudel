from __future__ import unicode_literals

from django.db import models

SITE_IDS = (
    (1, 'unisport.dk'),
    (10, 'unisportstore.se'),
    (11, 'unisportstore.com'),
    (12, 'unisportstore.no'),
    (13, 'unisportstore.fi'),
    (14, 'unisportstore.nl'),
    (15, 'unisportstore.de'),
    (16, 'unisportstore.fr'),
    (20, 'unisportstore.be'),
    (21, 'unisportstore.ch'),
    (22, 'unisportstore.at'),
    (23, 'unisportstore.pl')
)


class LocalBusiness(models.Model):
    site_id = models.IntegerField(choices=SITE_IDS)
    name = models.CharField(max_length=100, default=u'Unisport A/S')
    streetAddress = models.CharField(max_length=255, blank=True)
    addressLocality = models.CharField(max_length=100, blank=True)
    addressRegion = models.CharField(max_length=100, blank=True)
    postalCode = models.CharField(max_length=100, blank=True)
    addressCountry = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=100, blank=True)
    additional_text = models.CharField(max_length=255, blank=True)

    @property
    def site_name(self):
        return u'{0} - {1}'.format(self.name, dict(SITE_IDS)[self.site_id])

    def opening_hours(self):
        return OpeningHours.objects.filter(localbusiness_id=self.id).order_by('display_order')


class OpeningHours(models.Model):
    localbusiness = models.ForeignKey(LocalBusiness, on_delete=models.CASCADE)
    opening_hours = models.CharField(max_length=255)
    display_order = models.IntegerField(default=0)
