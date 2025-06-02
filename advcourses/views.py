from bootcamps.models import Bootcamp, BootcampRegistration, BootcampUser
from bootcamps.serialzers import BootcampSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from advcourses.models import AdvCourse, AdvCourseRegistration, AdvCourseUser
from advcourses.serializers import AdvCourseSerializer, AdvCourselistSerializer, AdvCourseRegistrationSerializer, AdvCourseUserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from bootcamps.tasks import send_approval_email, send_approval_sms
from accounts.permissions import HasRole
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class AdvCourseListVew(ListAPIView):
    queryset = AdvCourse.objects.all()
    serializer_class = AdvCourseSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'start_date']
    search_fields = ['title', 'description']

class AdvCourseRegisterView(CreateAPIView):
    queryset = AdvCourseRegistration.objects.all()
    serializer_class = AdvCourseRegistrationSerializer
    permission_classes = [AllowAny]


class ApproveAdvRegistrationView(APIView):
    permission_classes = [HasRole('support')]

    def post(self, request, pk):
        try:
            reg_request = AdvCourseRegistration.objects.get(pk=pk)

            if reg_request.status == 'approved':
                return Response({'detail': 'This registration has already been approved.'}, status=status.HTTP_400_BAD_REQUEST)

            advcourse = reg_request.advcourse
            if advcourse.members.count() >= advcourse.capacity:
                reg_request.status = 'rejected'
                reg_request.save()
                return Response({'detail': 'AdvCourse is full.'}, status=status.HTTP_400_BAD_REQUEST)

            user, _ = User.objects.get_or_create(
                phone=reg_request.phone,
                defaults={'full_name': reg_request.full_name}
            )

            AdvCourseUser.objects.create(
                advcourse=advcourse,
                user=user,
                role=reg_request.role
            )

            reg_request.status = 'approved'
            reg_request.save()

            send_approval_sms.delay(reg_request.phone, reg_request.full_name, advcourse.title)
            send_approval_email.delay(reg_request.email)

            return Response({'detail': 'User added and registration approved.'}, status=status.HTTP_200_OK)

        except AdvCourseRegistration.DoesNotExist:
            return Response({'detail': 'Registration request not found.'}, status=status.HTTP_404_NOT_FOUND)