# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursomod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechafinal', models.DateField()),
                ('horarioini', models.TimeField()),
                ('horariofin', models.TimeField()),
                ('dias', models.CharField(default='', max_length=500)),
                ('requisitos', models.CharField(default='', max_length=1000)),
                ('descripcion', models.CharField(default='', max_length=1000)),
                ('objetivos', models.CharField(default='', max_length=1000)),
                ('dirigido', models.CharField(default='', max_length=1000)),
                ('costo', models.CharField(default='', max_length=15)),
                ('costototal', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
