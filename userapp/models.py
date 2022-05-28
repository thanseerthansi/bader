# from django.db import models
from django.contrib.gis.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    mobile = models.CharField(max_length=100,blank=True)
    address = models.TextField(max_length=100,blank=True)
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='Image',blank=True)
    last_searched = models.CharField(max_length=200,blank=True)
    
    