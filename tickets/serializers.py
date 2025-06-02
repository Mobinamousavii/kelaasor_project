from rest_framework.serializers import ModelSerializer
from tickets.models import Ticket, Message

class TicketMessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'message', 'attachment', 'created_at']
        read_only_fields = ['id', 'created_at', 'sender']

class TicketSerializer(ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'user', 'related_bootcamp', 'status', 'created_at', 'messages']
        read_only_fields = ['id', 'user', 'status', 'created_at']

