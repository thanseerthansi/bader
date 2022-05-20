from django.contrib import admin
from propertyapp.models import PropertyTypesModel, PropertyModel


# Register your models here.
admin.site.register(PropertyTypesModel)
admin.site.register(PropertyModel)