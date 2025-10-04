from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Blog, CategoryBlog
from rest_framework import status



class BlogSerializer(serializers.ModelSerializer):
    blogcategory = serializers.SlugRelatedField(
        slug_field = "name",
        queryset = CategoryBlog.objects.all()
    )
    uploaded_by = serializers.StringRelatedField()
    class Meta:
        model = Blog
        fields = ["title", "content", "status", "blogcategory", "file", "uploaded_by"]
        read_only_fields = ["uploaded_by", "slug"]


    def create(self, validated_data):
        validated_data["uploaded_by"] = self.context["request"].user
        return Blog.objects.create(**validated_data)    
