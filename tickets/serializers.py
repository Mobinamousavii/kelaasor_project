from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from tickets.models import Ticket,TicketMessage

class TicketMessageSerializer(ModelSerializer):
    ticket_id = serializers.IntegerField(source='ticket.id', read_only=True)
    ticket_title = serializers.CharField(source='ticket.title', read_only=True)
    sender_name = serializers.CharField(source='sender.full_name', read_only=True)
    class Meta:
        model = TicketMessage
        fields = ['id', 'sender','ticket_id',  'ticket_title','sender_name', 'message', 'attachment', 'created_at']
        read_only_fields = ['id', 'created_at', 'sender', 'ticket_id', 'ticket_title', 'sender_name']
        
class TicketSerializer(ModelSerializer):
    messages = TicketMessageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'user', 'related_bootcamp', 'status', 'created_at', 'messages']
        read_only_fields = ['id', 'user', 'status', 'created_at']

