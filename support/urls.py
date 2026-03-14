from django.urls import path
from .views import email_reply_webhook

urlpatterns = [
    path('email-reply/', email_reply_webhook, name='email_reply'),
]