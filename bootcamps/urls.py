from django.urls import path
from bootcamps.views import BootcampListVew, BootcampRegisterView, ApproveRegistrationView, Mybootcamps

urlpatterns = [
    path('',BootcampListVew.as_view()),
    path('register/', BootcampRegisterView.as_view()),
    path('approve/<int:pk>/',ApproveRegistrationView.as_view()),
    path('my-bootcamps/', Mybootcamps.as_view()),
]
