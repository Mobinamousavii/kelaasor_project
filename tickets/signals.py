from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Ticket

@receiver(post_save, sender=Ticket)
def notify_admins_on_new_ticket(sender, instance, created, **kwargs):
    if not created:
        return  

    subject = f"📨 New Ticket Submitted: {instance.title}"
    message = f"User: {instance.user.full_name}\n" \
              f"Phone: {instance.user.phone}\n" \
              f"Title: {instance.title}\n\n" \
              f"Check in admin panel."

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [admin[1] for admin in settings.ADMINS] 

    send_mail(subject, message, from_email, recipient_list, fail_silently=True)