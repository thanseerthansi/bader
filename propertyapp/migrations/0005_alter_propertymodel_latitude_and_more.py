# Generated by Django 4.0.4 on 2022-05-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyapp', '0004_propertymodel_agent_likedpropertymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertymodel',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='longtitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=50, null=True),
        ),
    ]
