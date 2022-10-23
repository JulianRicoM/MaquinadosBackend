from pyexpat import model
from rest_framework import serializers

from Applications.employee.models import Employee, Eps, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eps
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    eps = EPSSerializer()
    position = PositionSerializer()
    class Meta:
        model = Employee
        fields = '__all__'