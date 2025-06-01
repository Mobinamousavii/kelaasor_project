from bootcamps.models import Bootcamp, BootcampRegistration, BootcampUser
from bootcamps.serialzers import BootcampSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from bootcamps.serialzers import BootcampSerializer, BootcampRegistrationSerializer, BootcampUserSerializer, BootcamplistSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from bootcamps.tasks import send_approval_email, send_approval_sms
from accounts.permissions import HasRole
class BootcampListVew(ListAPIView):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer
    permission_classes = [AllowAny]

class BootcampRegisterView(CreateAPIView):
    queryset = BootcampRegistration.objects.all()
    serializer_class = BootcampRegistrationSerializer
    permission_classes = [AllowAny]

class ApproveRegistrationView(APIView):
    permission_classes = [ HasRole('support')]

    def post(self, request, pk):
        try:
            reg_request = BootcampRegistration.objects.get(pk=pk)
            if reg_request.status == 'approved':
                return Response({'detail': 'قبلاً تایید شده'}, status=status.HTTP_400_BAD_REQUEST)
            
  
            bootcamp = reg_request.bootcamp
            if bootcamp.members.count() >= bootcamp.capacity:
                reg_request.status = 'rejected'
                reg_request.save()

                return Response({'detail': 'ظرفیت پر شده است.'}, status=status.HTTP_400_BAD_REQUEST)
            user, _ = User.objects.get_or_create(phone = reg_request.phone , defaults={'full_name': reg_request.full_name})

            BootcampUser.objects.create(
                bootcamp = bootcamp,
                user = user, 
                role = reg_request.role
            )
            reg_request.status = 'approved'
            reg_request.save()

            send_approval_sms.delay(reg_request.phone, reg_request.full_name, bootcamp.title)
            send_approval_email.delay(reg_request.email)

            return Response({'detail': 'User added and registration approved.'}, status=status.HTTP_200_OK)
        
        except BootcampRegistration.DoesNotExist:
            return Response ({'detail': 'Registration request not found.'}, status=status.HTTP_404_NOT_FOUND)
        
class Mybootcamps(ListAPIView):
    serializer_class = BootcamplistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bootcamp.objects.filter(members__user = self.request.user).distinct()


