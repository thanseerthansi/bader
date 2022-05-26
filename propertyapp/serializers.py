from rest_framework import serializers
from .models import *

# class PropertyTypesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PropertyTypesModel
#         fields = '__all__'
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'
class LikedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedPropertyModel
        fields = '__all__'


