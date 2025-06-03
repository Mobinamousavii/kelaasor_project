from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from payments.models import Payment, Invoice

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'user', 'amount', 'related_bootcamp', 'related_advcourse', 'created_at', 'is_fully_paid']
        read_only_fields = ['user', 'created_at', 'is_fully_paid']

        def get_is_fully_paid(self, obj):
            return obj.is_fully_paid()
        
class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'invoice', 'amount', 'payment_type', 'tracking_code', 'receipt_image', 'created_at']
        read_only_fields = ['created_at']

        

