from rest_framework import serializers

from Applications.client.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ["is_active"]
