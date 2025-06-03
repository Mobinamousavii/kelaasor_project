from django.contrib import admin
from .models import Ticket, TicketMessage

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['title', 'user__phone']
    ordering = ['-created_at']

@admin.register(TicketMessage)
class TicketMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket', 'sender', 'created_at']
    search_fields = ['ticket__title', 'sender__phone']
    ordering = ['-created_at']