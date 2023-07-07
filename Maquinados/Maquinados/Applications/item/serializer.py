from dataclasses import fields
from rest_framework import serializers
from Applications.item.models import Item, Material, Measurement_units

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Material
        fields = '__all__'
        
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement_units
        fields = '__all__'

        