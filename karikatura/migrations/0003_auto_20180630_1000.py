# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karikatura', '0002_auto_20180629_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
