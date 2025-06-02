from rest_framework.serializers import ModelSerializer
from advcourses.models import AdvCourse, AdvCourseRegistration, AdvCourseUser
from rest_framework import serializers
from bootcamps.base_serializers import BaseRegistrationSerializer
import logging

logger = logging.getLogger(__name__)

class AdvCourseSerializer(ModelSerializer):
    class Meta:
        model = AdvCourse
        fields = '__all__'
        read_only_fields = ['status', 'created_at']


class AdvCourseRegistrationSerializer(BaseRegistrationSerializer):
    class Meta:
        model = AdvCourseRegistration
        fields = ['id', 'advcourse', 'full_name', 'phone', 'email', 'role', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
        event_field = 'advcourse'

class AdvCourseUserSerializer(ModelSerializer):
    class Meta:
        model = AdvCourseUser
        fields = '__all__'
    

class AdvCourselistSerializer(ModelSerializer):
    class Meta:
        model = AdvCourse
        fields = [ 'title', 'start_date', 'end_date', 'status']