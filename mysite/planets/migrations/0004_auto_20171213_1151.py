# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0003_auto_20171213_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planets',
            name='planet_mass_to_earth',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10, verbose_name='planet mass relative to an Earth'),
        ),
    ]