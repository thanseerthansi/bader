# from django.db import models
from django.contrib.gis.db import models
from userapp.models import UserModel


# Create your models here.
# class PropertyTypesModel(models.Model):
#     types = models.CharField(max_length=20)
#     description = models.TextField()

class PropertyModel(models.Model):
    agent = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True)
    property_type = models.CharField(max_length=100)
    residential_type = models.CharField(max_length=100,null=True)
    property_name =  models.CharField(max_length=100)
    property_radious = models.FloatField(default=0.0,blank=True)
    property_bed = models.FloatField(default=0.0,blank=True,null=True)
    property_room = models.FloatField(default=0.0,blank=True,null=True)
    property_bath = models.FloatField(default=0.0,blank=True,null=True)
    property_price = models.FloatField(default=0.0,blank=True)
    property_purpose = models.CharField(max_length=100)
    property_city = models.CharField(max_length=100)
    added_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    location = models.PointField(geography=True, blank=True, null=True)
    broucher = models.FileField(upload_to='files',blank=True,null=True)
    video = models.FileField(upload_to='files',blank=True,null=True)
    
class LikedPropertyModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    liked_property = models.ManyToManyField(PropertyModel)
    created_date =  models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)

class ImagesModel(models.Model):
    property_id = models.ForeignKey(PropertyModel,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='Image',blank=True)
    image_purpose = models.CharField(max_length=100)
    created_date =  models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class UtilitiesModel(models.Model):
    property = models.ForeignKey(PropertyModel,on_delete=models.CASCADE)
    utility = models.CharField(max_length=100)
    far = models.FloatField(default=0.0)
    
