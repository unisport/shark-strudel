# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localbusiness', '0002_localbusiness_additional_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='localbusiness',
            name='site_id',
            field=models.IntegerField(default=0),
        ),
    ]
