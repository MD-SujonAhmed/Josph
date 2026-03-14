from django.contrib import admin
from .models import BusinessFAQ, AIEmailLog

@admin.register(BusinessFAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

@admin.register(AIEmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'created_at')