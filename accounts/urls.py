from django.urls import path
from accounts.views import SignupView,ProfileView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    # path('otp/request/',RequestOTPView.as_view()),
    # path('otp/verify/', VerifyOTPView.as_view()),
    path('profile/', ProfileView.as_view()),
]
