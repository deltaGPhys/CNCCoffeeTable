# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pattern',
            name='Type',
            field=models.CharField(choices=[('Background', 'Background'), ('Shape', 'Shape')], default='Textual', max_length=30),
        ),
    ]
