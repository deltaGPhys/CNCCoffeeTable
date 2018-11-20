# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_pattern_gcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='Duration',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='Gcode',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]