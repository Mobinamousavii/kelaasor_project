from django.urls import path
from bootcamps.views import BootcampListVew, BootcampRegisterView

urlpatterns = [
    path('',BootcampListVew.as_view()),
    path('register/', BootcampRegisterView.as_view()),

]
