from django.urls import path
from .views import CreateBlogView


urlpatterns = [
    path("upload/", CreateBlogView.as_view(), name="upload-blog")
]
