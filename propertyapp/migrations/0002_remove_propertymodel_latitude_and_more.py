# Generated by Django 4.0.4 on 2022-05-26 05:16

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('propertyapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertymodel',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='propertymodel',
            name='longitude',
        ),
        migrations.AddField(
            model_name='propertymodel',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
