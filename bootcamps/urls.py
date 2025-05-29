from django.urls import path
from bootcamps.views import BootcampListVew, BootcampRegisterView, ApproveRegistrationView

urlpatterns = [
    path('',BootcampListVew.as_view()),
    path('register/', BootcampRegisterView.as_view()),
    path('approve/<int:pk>/',ApproveRegistrationView.as_view()),
    

]
