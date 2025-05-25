from rest_framework.serializers import ModelSerializer, Serializer
from bootcamps.models import Bootcamp, BootcampUser, BootcampRegistrationRequest

class BootcampSerializer(ModelSerializer):
    class Meta:
        model = Bootcamp
        fields = '__all__'
        read_only_fields = ['status', 'created_at']

class BootcampRegistrationRequestSerialzer(ModelSerializer):
    class Meta:
        model = BootcampRegistrationRequest
        fields = ['id', 'bootcamp', 'full_name', 'phone', 'national_code', 'email', 'role']

class BootcampUserSerialzer(ModelSerializer):
    class Meta:
        model = BootcampUser
        fields = '__all__'
