from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from accounts.models import User, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken
    
class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'national_code', 'gender', 'birth_date'] 
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'national_code': {'required': False},
            'gender': {'required': False},
            'birth_date': {'required': False},
        }

class UserSerializer(ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'is_active', 'full_name', 'is_staff', 'data_joined']
        read_only_fields = ['id', 'is_active', 'is_staff', 'data_joined']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    

        


