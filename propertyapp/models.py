from tkinter import CASCADE
from django.db import models

from userapp.models import UserModel

# Create your models here.
class PropertyTypesModel(models.Model):
    types = models.CharField(max_length=20)
    description = models.TextField()

from math import radians, cos, sin, asin, sqrt
class PropertyModel(models.Model):
    agent = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    property_type = models.ForeignKey(PropertyTypesModel,on_delete=models.CASCADE)
    property_name =  models.CharField(max_length=50)
    property_radious = models.FloatField(default=0.0,blank=True)
    property_price = models.FloatField(default=0.0,blank=True)
    property_purpose = models.CharField(max_length=10)
    property_city = models.CharField(max_length=50)
    added_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16,blank=True,null=True)
    longitude =  models.DecimalField(max_digits=22, decimal_places=16,blank=True,null=True)
class LikedPropertyModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    liked_property = models.ManyToManyField(PropertyModel)
   
    
