from bootcamps.models import Bootcamp, BootcampRegistrationRequest, BootcampUser
from bootcamps.serialzers import BootcampSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from bootcamps.serialzers import BootcampSerializer, BootcampRegistrationRequestSerialzer, BootcampUserSerialzer
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.permissions import IsSupportOrSuperuser
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_approval_sms

class BootcampListVew(ListAPIView):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer
    permission_classes = [AllowAny]

class BootcampRegisterView(CreateAPIView):
    queryset = BootcampRegistrationRequest.objects.all()
    serializer_class = BootcampRegistrationRequestSerialzer
    permission_classes = [AllowAny]

class ApproveRegistrationView(APIView):
    permission_classes = [IsSupportOrSuperuser]

    def post(self, request, pk):
        try:
            reg_request = BootcampRegistrationRequest.objects.get(pk=pk)
            if reg_request.status == 'approved':
                return Response({'detail': 'قبلاً تایید شده'}, status=status.HTTP_400_BAD_REQUEST)
            
            user, _ = User.objects.get_or_create(phone = reg_request.phone, defaults={'full_name' : reg_request.full_name})

            reg_request.status = 'approved'
            reg_request.save()

            send_approval_sms.delay(
                phone = reg_request.phone,
                full_name = reg_request.full_name,
                bootcamp_title = reg_request.bootcamp.titl
            )

            return Response({'detail': 'ثبت‌ نام تایید شد و پیامک ارسال شد.'}, status=status.HTTP_200_OK)
        except BootcampRegistrationRequest.DoesNotExist:
            return Response({'detail': 'درخواست یافت نشد'}, status=status.HTTP_404_NOT_FOUND)


