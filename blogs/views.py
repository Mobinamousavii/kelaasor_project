from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CategoryBlog, Blog
from rest_framework.response import Response
from accounts.permissions import HasRole
from .serializers import BlogSerializer
from django.db import transaction



class CreateBlogView(APIView):
    permission_classes = [HasRole('support')]

    @transaction.atomic    
    def post(self, request):
            serializer = BlogSerializer(data=request.data, context={"request":request})
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




