from kavenegar import KavenegarAPI, APIException, HTTPException
import os
from django.core.cache import  caches
from django.conf import settings
import random
import logging

logger =logging.getLogger(__name__)
otp_cache = caches['otp_cache']

def send_otp_sms(phone, otp_code):
    try:
        api_key = os.getenv('KAVEHNEGAR_API_KEY')
        if not api_key:
            logger.error("KAVEHNEGAR_API_KEY environment variable not set.")
            return False
        
        api = KavenegarAPI(api_key)
        params = {
            'sender': '2000660110',  
            'receptor':phone,
            'message': f'کد ورود شما به کلاسور: {otp_code}',
        }
        response = api.sms_send(params)
        logger.info("SMS sent:", response)
        return True
    except APIException as e:
        logger.error('API Exception:', e)
        return False
    except HTTPException as e:
        logger.error('HTTP Exception:', e)
        return False

def generate_otp():
    return str(random.randint(100000, 999999))

def store_otp(phone, otp_code):
    key = f"otp_{phone}"
    timeout = settings.OTP_TIMEOUT
    otp_cache.set(key, otp_code, timeout=timeout)
    logger.info(f"OTP for {phone} stored in cache with key {key} for {timeout} seconds.")
    return True

def get_otp(phone):
    key = f"otp_{phone}"
    otp = otp_cache.get(key)
    if otp:
        logger.info(f"OTP retrieved from cache for {phone}.")
    else:
        logger.warning(f"No OTP found in cache for {phone}. It might have expired or never been set.")
    return otp

def delete_otp(phone):
    key = f"otp_{phone}" 
    otp_cache.delete(key)
    logger.info(f"OTP for {phone} deleted from cache.")

def verify_otp(phone, input_code):
    stored_otp = get_otp(phone)

    if stored_otp and stored_otp == input_code:
        delete_otp(phone)
        logger.info(f"OTP verification successful for {phone}.")
        return True
    else:
        logger.warning(f"OTP verification failed for {phone}. Stored: {stored_otp}, Entered: {input_code}")
        return False