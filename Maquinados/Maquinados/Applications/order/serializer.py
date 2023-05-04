from rest_framework import serializers

from .models import Order, OrderProcess,  Currency, PaymentMethod

from  Applications.quote.serializer import ListQuoteSerializer

class OrderProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProcess
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class ListOrderSerializer(serializers.ModelSerializer):
    process_id = OrderProcessSerializer()
    currency = CurrencySerializer()
    payment_method = PaymentSerializer()
    quote_number = ListQuoteSerializer()
    class Meta:
        model = Order
        fields = '__all__'