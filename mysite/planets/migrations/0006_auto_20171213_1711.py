# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0005_planets_planet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='planets',
            name='planet_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='planets',
            name='planet_mass_to_earth',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, verbose_name='planet mass relative to an Earth'),
        ),
        migrations.AlterField(
            model_name='planets',
            name='satellites',
            field=models.PositiveSmallIntegerField(blank=True, default=None),
        ),
    ]