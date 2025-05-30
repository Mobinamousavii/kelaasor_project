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


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class RequestOTPView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         phone = request.data.get('phone')
#         if not phone:
#             return Response({'error': 'Phone number is required.'}, status=status.HTTP_400_BAD_REQUEST)

#         otp_code = str(random.randint(100000, 999999))

#         OTPCode.objects.create(
#             phone=phone,
#             code=otp_code,
#             expires_at=timezone.now() + timedelta(minutes=2)
#         )
#         print("OTP code is:", otp_code)
#         send_otp_task.delay(phone, otp_code)

#         return Response({'message': 'کد تایید ارسال شد.'}, )
    

# class VerifyOTPView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = OTPVerifySerializer(data=request.data)
#         if serializer.is_valid():
#             tokens = serializer.save()
#             return Response(tokens, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
    

