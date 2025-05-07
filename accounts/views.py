from accounts.models import User
from rest_framework.generics import CreateAPIView
from accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
