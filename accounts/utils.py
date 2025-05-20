from kavenegar import KavenegarAPI, APIException, HTTPException
import os

def send_otp_sms(phone_number, otp_code):
    try:
        api_key = os.getenv('KAVEHNEGAR_API_KEY')
        if not api_key:
            raise ValueError("KAVEHNEGAR_API_KEY environment variable not set.")
        
        api = KavenegarAPI(api_key)
        params = {
            'sender': '2000660110',  
            'receptor':phone_number,
            'message': f'کد ورود شما به کلاسور: {otp_code}',
        }
        response = api.sms_send(params)
        print("SMS sent:", response)
        return response
    except APIException as e:
        print('API Exception:', e)
    except HTTPException as e:
        print('HTTP Exception:', e)