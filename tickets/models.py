from django.db import models
from django.conf import settings

class Ticket(models.Model):
    STATUS_CHOICES = (
        ('pending', 'پاسخ داده نشده'),
        ('reviewing', 'در حال بررسی'),
        ('answered', 'پاسخ داده شده'),
        ('closed', 'بسته شده'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    title = models.CharField(max_length=255)
    related_bootcamp = models.ForeignKey('bootcamps.Bootcamp', on_delete=models.SET_NULL, null=True, blank=True)
    related_advcourse = models.ForeignKey('advcourses.AdvCourse', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket #{self.id} - {self.title}'
    
class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    attachment = models.FileField(upload_to='ticket_attachments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.sender.phone} on Ticket #{self.ticket.id}'