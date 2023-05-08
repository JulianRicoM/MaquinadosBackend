from rest_framework import serializers

from .models import Quote, StatusQuote
from Applications.client.serializer import ClientSerializer
from Applications.item.serializer import ItemSerializer

class ListQuoteSerializer(serializers.ModelSerializer):
    client_id = ClientSerializer()
    item_id = ItemSerializer()
    class Meta:
        model = Quote
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class StatusQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusQuote
        fields = '__all__'