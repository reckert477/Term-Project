# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_auto_20161205_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='average',
            field=models.DecimalField(decimal_places=10, default=7.5, max_digits=15),
        ),
    ]