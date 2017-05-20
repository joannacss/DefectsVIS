# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defects', '0004_auto_20170507_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defect',
            name='blocks',
        ),
        migrations.AddField(
            model_name='defect',
            name='blocks',
            field=models.ManyToManyField(related_name='blockers', to='defects.Defect'),
        ),
        migrations.RemoveField(
            model_name='defect',
            name='depends',
        ),
        migrations.AddField(
            model_name='defect',
            name='depends',
            field=models.ManyToManyField(related_name='depends_on', to='defects.Defect'),
        ),
    ]
