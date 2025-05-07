from rest_framework.serializers import ModelSerializer
from accounts.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'is_active', 'full_name', 'is_staff', 'data_joined']
        read_only_fields = ['id', 'is_active', 'is_staff', 'data_joined']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"