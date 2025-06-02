from django.urls import path
from advcourses.views import AdvCourseListVew

urlpatterns = [
    path('', AdvCourseListVew.as_view()),
]
