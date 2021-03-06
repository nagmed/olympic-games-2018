# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import main.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_chump_about_short'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamousOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('about_short', models.TextField(default='Good guy and all', max_length=128, verbose_name='Very brief description')),
                ('specialty', models.TextField(verbose_name='Specialty')),
                ('achievements', models.TextField(verbose_name='Achievements')),
                ('image', models.ImageField(default='no_image.png', upload_to=main.models.utils.make_filepath, verbose_name='news image')),
            ],
        ),
    ]
