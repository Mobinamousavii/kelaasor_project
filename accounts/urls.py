from django.urls import path
from accounts.views import SignupView, RequestOTPView, VerifyOTPView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('otp/request/',RequestOTPView.as_view()),
    path('otp/verify/', VerifyOTPView.as_view()),
]
