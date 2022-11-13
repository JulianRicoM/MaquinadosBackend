from rest_framework import serializers

from .models import Quote, StatusQuote
from Applications.client.serializer import ClientSerializer

class QuoteSerializer(serializers.ModelSerializer):
    #client_id = ClientSerializer() -> uncomment if you want to throw the customer info in the quote
    class Meta:
        model = Quote
        fields = '__all__'

class StatusQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusQuote
        fields = ('status_description',)