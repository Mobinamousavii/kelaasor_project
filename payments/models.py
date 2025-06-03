from django.db import models
from django.conf import settings

class Invoice(models.Model):
    STATUS_CHOICES = (
        ('unpaid', 'پرداخت نشده'),
        ('pending_review', 'در انتظار بررسی'),
        ('paid', 'پرداخت شده'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='billing_records')
    related_bootcamp = models.ForeignKey('bootcamps.Bootcamp', on_delete=models.SET_NULL, null=True, blank=True)
    related_advcourse = models.ForeignKey('advcourses.AdvCourse', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='unpaid')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.user.phone} - {self.amount} تومان"

    def is_fully_paid(self):
        total_paid = sum(payment.amount for payment in self.payments.all())
        return total_paid >= self.amount
    



class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('offline', 'Offline'),
        ('online', 'Online'),
    )

    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    tracking_code = models.CharField(max_length=50, blank=True)
    receipt_image = models.ImageField(upload_to='receipts/', null=True, blank=True)
    note = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id} for Invoice #{self.invoice.id}"