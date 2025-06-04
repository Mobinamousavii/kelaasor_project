from django.contrib import admin
from .models import Invoice, Payment

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__phone', 'related_bootcamp__title', 'related_advcourse__title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'amount', 'payment_method', 'tracking_code', 'submitted_at')
    list_filter = ('payment_method', 'submitted_at')
    search_fields = ('invoice__user__phone', 'tracking_code')
    readonly_fields = ('submitted_at',)
    ordering = ('-submitted_at',)
