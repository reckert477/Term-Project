# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_anime_alltags'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='context',
            field=models.CharField(default=b'', max_length=500),
        ),
    ]
