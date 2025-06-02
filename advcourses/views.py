from bootcamps.models import Bootcamp, BootcampRegistration, BootcampUser
from bootcamps.serialzers import BootcampSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from advcourses.models import AdvCourse, AdvCourseRegistration, AdvCourseUser
from advcourses.serializers import AdvCourseSerializer, AdvCourselistSerializer, AdvancedCourseRegistrationSerializer, AdvCourseUserSerializer
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


