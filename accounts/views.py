from accounts.models import User 
from rest_framework.generics import CreateAPIView , RetrieveAPIView , RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import UserSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from accounts.tasks import send_otp_task
import random
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from accounts.utils import generate_otp, store_otp , send_otp_sms, verify_otp
import logging

logger = logging.getLogger(__name__)


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class RequestOTPView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        phone = request.data.get('phone')

        if not phone:
            return Response({"detail": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        otp_code = generate_otp()
        store_otp(phone, otp_code)

        success = send_otp_sms(phone, otp_code)
        if not success:
            logger.error(f"SendOtpAPIView: Failed to send OTP SMS for {phone}.")
            return Response({"detail": "Failed to send OTP SMS. Please try again."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        logger.info(f"RequestOTPView: OTP requested and sent successfully for phone: {phone}.")
        return Response({"detail": "OTP sent successfully."}, status=status.HTTP_200_OK)

    

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        phone = request.data.get('phone')
        code = request.data.get('code')

        if not phone and not code:
            return Response({"detail": "Phone number and OTP code are required."}, status=status.HTTP_400_BAD_REQUEST)
        
        success, message = verify_otp(phone , code)
        if not success:
            return Response({"detail": message}, status=status.HTTP_400_BAD_REQUEST)
        
        user, _ = User.objects.get_or_create(phone=phone)

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_200_OK)



class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    

