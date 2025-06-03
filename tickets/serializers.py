from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket,TicketMessage

class TicketMessageSerializer(ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = ['id', 'sender', 'message', 'attachment', 'created_at']
        read_only_fields = ['id', 'created_at', 'sender']

class TicketSerializer(ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'user', 'related_bootcamp', 'status', 'created_at', 'messages']
        read_only_fields = ['id', 'user', 'status', 'created_at']

