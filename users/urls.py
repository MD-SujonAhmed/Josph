from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    LoginView,
    ForgotPasswordView,
    VerifyOTPView,
    ResendOTPView,
    FAQViewSet,
    LogoutView,
    ResetPasswordView
    

)
router=DefaultRouter()
router.register(r'faq',FAQViewSet,basename='faq')

urlpatterns=router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend-otp'),
    path('new_password/', ResetPasswordView.as_view(), name='resend-otp'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
