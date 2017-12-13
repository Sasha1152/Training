# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0006_auto_20171213_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moons',
            fields=[
                ('moon_number', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('moon_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'moon',
                'verbose_name_plural': 'moons',
                'ordering': ['moon_number'],
            },
        ),
        migrations.RemoveField(
            model_name='planets',
            name='satellites',
        ),
        migrations.AddField(
            model_name='planets',
            name='moons_quantity',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='moons',
            name='planet_mother',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planets.Planets'),
        ),
    ]
