# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-07-17 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_school_updatedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]