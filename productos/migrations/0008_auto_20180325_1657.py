# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20180325_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
