# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 10:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models.projects.university_saturdays


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_event_isclosed'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='N/A', max_length=255, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='event',
            name='subject',
            field=models.ForeignKey(default=main.models.projects.university_saturdays.subject_default, editable=False, on_delete=django.db.models.deletion.CASCADE, to='main.Subject', verbose_name='Subject'),
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ManyToManyField(to='main.EventType', verbose_name='Event type'),
        ),
    ]