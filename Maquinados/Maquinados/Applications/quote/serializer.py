from rest_framework import serializers

from .models import Quote
from Applications.client.models import Client

class QuoteSerializer(serializers.ModelSerializer):
    nit = Client()
    class Meta:
        model = Quote
        fields = '__all__'