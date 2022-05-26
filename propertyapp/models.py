# from django.db import models
from django.contrib.gis.db import models
from userapp.models import UserModel

# Create your models here.
# class PropertyTypesModel(models.Model):
#     types = models.CharField(max_length=20)
#     description = models.TextField()

class PropertyModel(models.Model):
    agent = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    property_type = models.CharField(max_length=20)
    residential_type = models.CharField(max_length=20,null=True)
    property_name =  models.CharField(max_length=50)
    property_radious = models.FloatField(default=0.0,blank=True)
    property_bed = models.FloatField(default=0.0,blank=True,null=True)
    property_room = models.FloatField(default=0.0,blank=True,null=True)
    property_bath = models.FloatField(default=0.0,blank=True,null=True)
    property_price = models.FloatField(default=0.0,blank=True)
    property_purpose = models.CharField(max_length=10)
    property_city = models.CharField(max_length=50)
    added_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    location = models.PointField(geography=True, blank=True, null=True)
    # images = models.ForeignKey()
    # floorplans  = models.
class LikedPropertyModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    liked_property = models.ManyToManyField(PropertyModel)
   
    
