# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appesi', '0007_auto_20171109_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadoramod',
            name='imagen',
        ),
    ]
