from rest_framework.serializers import ModelSerializer, Serializer
from bootcamps.models import Bootcamp, BootcampUser, BootcampRegistration
from rest_framework import serializers
from bootcamps.base_serializers import BaseRegistrationSerializer
import logging

logger = logging.getLogger(__name__)

class BootcampSerializer(ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = '__all__'
        read_only_fields = ['status', 'created_at']

class BootcampRegistrationSerializer(BaseRegistrationSerializer):
    class Meta:
        model = BootcampRegistration
        fields = ['id', 'bootcamp', 'full_name', 'phone', 'email', 'role', 'status', 'created_at']
        read_only_fields = ['created_at', 'status']
        event_field = 'bootcamp'

class BootcampUserSerializer(ModelSerializer):
    class Meta:
        model = BootcampUser
        fields = '__all__'

class BootcamplistSerializer(ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = [ 'title', 'start_date', 'end_date', 'status']