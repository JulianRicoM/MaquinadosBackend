from rest_framework import serializers

from .models import Tools, StatusTools

class StatusToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTools
        fields = '__all__'
class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'