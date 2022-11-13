from rest_framework import serializers

from .models import Order, OrderProcess, OrderStatus, Currency, PaymentMethod

class OrderProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProcess
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
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
    process_id = OrderProcessSerializer()
    status_id = OrderStatusSerializer()
    currency = CurrencySerializer()
    payment_method = PaymentSerializer()
    class Meta:
        model = Order
        fields = '__all__'