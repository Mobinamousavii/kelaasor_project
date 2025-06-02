from django.urls import path
from advcourses.views import AdvCourseListVew , AdvCourseRegisterView , ApproveAdvRegistrationView, Myadvcourses

urlpatterns = [
    path('', AdvCourseListVew.as_view()),
    path('register/', AdvCourseRegisterView.as_view()),
    path('approve/<int:pk>/', ApproveAdvRegistrationView.as_view()),
    path('my-advcourses/', Myadvcourses.as_view()),
]
