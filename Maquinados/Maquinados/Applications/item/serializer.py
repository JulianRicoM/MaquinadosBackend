from dataclasses import fields
from rest_framework import serializers
from Applications.item.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'