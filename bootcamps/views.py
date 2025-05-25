from bootcamps.models import Bootcamp, BootcampRegistrationRequest, BootcampUser
from bootcamps.serialzers import BootcampSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from bootcamps.serialzers import BootcampSerializer, BootcampRegistrationRequestSerialzer, BootcampUserSerialzer
from rest_framework.permissions import IsAuthenticated, AllowAny

class BootcampListVew(ListAPIView):
    queryset = Bootcamp.objects.all()
    serializer_class = BootcampSerializer
    permission_classes = [AllowAny]

class BootcampRegisterView(CreateAPIView):
    queryset = BootcampRegistrationRequest.objects.all()
    serializer_class = BootcampRegistrationRequestSerialzer
    permission_classes = [AllowAny]


