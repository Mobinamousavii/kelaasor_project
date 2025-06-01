from rest_framework.serializers import ModelSerializer, Serializer
from bootcamps.models import Bootcamp, BootcampUser, BootcampRegistration
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)

class BootcampSerializer(ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = '__all__'
        read_only_fields = ['status', 'created_at']

class BootcampRegistrationSerializer(ModelSerializer):
    class Meta:
        model = BootcampRegistration
        fields = ['id', 'bootcamp', 'full_name', 'phone', 'email', 'role', 'status', 'created_at']
        read_only_fields = ['created_at', 'status']

    def validate(self, data):
        bootcamp = data['bootcamp']
        phone = data['phone']

        if bootcamp.status != 'registration_open':
            logger.warning(f"User with phone {phone} tried to register for bootcamp '{bootcamp.title}' with status '{bootcamp.status}'")
            raise serializers.ValidationError("Registration is only allowed for bootcamps with 'registration_open' status.")
        
        existing_request = BootcampRegistration.objects.filter(bootcamp= bootcamp, phone= phone)
        if existing_request.exists():
            logger.warning(f"Duplicate registration attempt by phone {phone} for bootcamp '{bootcamp.title}'")
            raise serializers.ValidationError("You have already submitted a request for this bootcamp.")
        
        return data

class BootcampUserSerializer(ModelSerializer):
    class Meta:
        model = BootcampUser
        fields = '__all__'

class BootcamplistSerializer(ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = [ 'title', 'start_date', 'end_date', 'status']