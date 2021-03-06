# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-17 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Blueprint', models.FileField(blank=True, null=True, upload_to=b'')),
                ('Photo', models.FileField(blank=True, null=True, upload_to=b'')),
                ('Duration', models.TimeField()),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
