from tkinter import CASCADE
from django.db import models

# Create your models here.
class PropertyTypesModel(models.Model):
    types = models.CharField(max_length=20)
    description = models.TextField()

class PropertyModel(models.Model):
    property_type = models.ForeignKey(PropertyTypesModel,on_delete=models.CASCADE)
    property_name =  models.CharField(max_length=50)
    property_radious = models.FloatField(default=0.0,blank=True)
    property_price = models.FloatField(default=0.0,blank=True)
    property_purpose = models.CharField(max_length=10)
    property_city = models.CharField(max_length=50)
    added_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    #needed property loation ..............
