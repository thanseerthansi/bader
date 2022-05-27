# Generated by Django 4.0.4 on 2022-05-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_usermodel_prof_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='prof_image',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='address',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='logo',
            field=models.ImageField(blank=True, upload_to='Image'),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='mobile',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]