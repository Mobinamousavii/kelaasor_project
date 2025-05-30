from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from accounts.models import User, UserProfile
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'is_active', 'full_name', 'is_staff', 'data_joined']
        read_only_fields = ['id', 'is_active', 'is_staff', 'data_joined']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
# class OTPVerifySerializer(Serializer):
#     phone = serializers.CharField(required=True)
#     otp = serializers.CharField(required=True)

#     def validate(self, data):
#         phone = data['phone']
#         otp= data['otp']

#         try:
#             otp = OTPCode.objects.filter(phone=phone, code = otp).latest('created_at')
#         except OTPCode.DoesNotExist:
#             raise serializers.ValidationError("کد وارد شده صحیح نیست.")
        
#         if hasattr(otp, 'is_expired') and otp.is_expired():
#             raise serializers.ValidationError("کد منقضی شده است.")

#         otp.is_used = True
#         otp.save()

#         user, created = User.objects.get_or_create(phone=phone)
#         data['user'] = user
#         return data

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
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



        


