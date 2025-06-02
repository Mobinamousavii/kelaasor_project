from celery import shared_task
from kavenegar import KavenegarAPI, HTTPException, APIException
import os
import logging
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

@shared_task
def send_approval_sms(phone, name, course_title):
    try:
        api_key = os.getenv('KAVEHNEGAR_API_KEY')
        if not api_key:
            logger.error("KAVEHNEGAR_API_KEY not set.")
            return False

        api = KavenegarAPI(api_key)
        message = f"{name} عزیز، ثبت‌نام شما در بوتکمپ {course_title} تایید شد."
        params = {
            'receptor': phone,
            'message': message,
            'sender': '2000660110',
        }
        response = api.sms_send(params)
        print(f"SMS sent to {phone}: {response}")
        return True
    except (APIException, HTTPException) as e:
        logger.error(f"SMS send error: {e}")
        return False

@shared_task 
def send_approval_email(email):
    try:
        if not email:
            logger.warning("No email address provided for email approval.")
            return False
        
        subject = 'Bootcamp Registration Approved'
        message = 'Your registration for the bootcamp has been approved. Welcome!'
        from_email = 'kelaasor@gmail.com'

        send_mail( subject, message, from_email, [email])
        logger.info(f"Email sent to {email}")

    except Exception as e:
        logger.error(f"Email send error: {e}")
        return False

    
    
