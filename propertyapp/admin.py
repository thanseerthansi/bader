from django.contrib import admin
from propertyapp.models import ImagesModel, LikedPropertyModel,  PropertyModel


# Register your models here.
admin.site.register(ImagesModel)
admin.site.register(PropertyModel)
admin.site.register(LikedPropertyModel)