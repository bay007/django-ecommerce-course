# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
