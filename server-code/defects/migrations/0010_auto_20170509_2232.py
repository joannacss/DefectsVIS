# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defects', '0009_defect_open_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='defect',
            name='closed_date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defect',
            name='fixed_by',
            field=models.CharField(default='casa', max_length=100),
            preserve_default=False,
        ),
    ]
