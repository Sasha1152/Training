# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planets', '0004_auto_20171219_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='moon',
            name='discovery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planet',
            name='discovery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moon',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]