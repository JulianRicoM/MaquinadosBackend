from rest_framework import serializers

from Applications.client.models import Client, Country, City, Department

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ["is_active"]
    
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
