from django.contrib import admin
from propertyapp.models import LikedPropertyModel,  PropertyModel


# Register your models here.
# admin.site.register(PropertyTypesModel)
admin.site.register(PropertyModel)
admin.site.register(LikedPropertyModel)