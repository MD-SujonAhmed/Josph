from django.urls import path
from .views import (
    LoginView,
    ForgotPasswordView,
    VerifyOTPView,
    ResendOTPView,

)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend-otp'),
]