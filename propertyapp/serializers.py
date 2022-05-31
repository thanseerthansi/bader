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
    liked_property = PropertySerializer(many=True)
    class Meta:
        model = LikedPropertyModel
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'

class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilitiesModel
        fields = '__all__'



