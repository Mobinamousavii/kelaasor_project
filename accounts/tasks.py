from celery import shared_task
from .utils import send_otp_sms

@shared_task
def send_otp_task(phone_number, otp_code):
    return send_otp_sms(phone_number, otp_code)