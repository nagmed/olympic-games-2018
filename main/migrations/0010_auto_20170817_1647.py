# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models
import main.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170816_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='no_image.png', upload_to=main.models.utils.make_filepath, verbose_name='news image'),
        ),
    ]
