from celery import shared_task
from kavenegar import KavenegarAPI
import os

@shared_task
def send_approval_sms(phone, name, bootcamp_title):
    try:
        api_key = os.getenv('KAVEHNEGAR_API_KEY')
        api = KavenegarAPI(api_key)
        message = f"{name} عزیز، ثبت‌نام شما در بوتکمپ {bootcamp_title} تایید شد."
        params = {
            'receptor': phone,
            'message': message,
            'sender': '2000660110',
        }
        response = api.sms_send(params)
        print("SMS sent:", response)
        return response
    except Exception as e:
        print("SMS Error:", e)
        return None