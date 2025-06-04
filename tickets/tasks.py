from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings

def notify_support_about_ticket(ticket):
    User = get_user_model()
    support_users = User.objects.filter(role__name='support') 
    support_emails = [user.email for user in support_users if user.email]

    if support_emails:
        subject = f"تیکت جدید از {ticket.user.full_name or ticket.user.phone}"
        message = f"یک تیکت جدید با عنوان '{ticket.title}' ثبت شده است.\n\nبرای مشاهده به پنل ادمین مراجعه کنید."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, support_emails)
        