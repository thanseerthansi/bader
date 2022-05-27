# Generated by Django 4.0.4 on 2022-05-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyapp', '0005_likedpropertymodel_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesmodel',
            name='image_purpose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='property_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='property_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='property_purpose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='property_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='propertymodel',
            name='residential_type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
