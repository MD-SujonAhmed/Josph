from rest_framework import serializers
from .models import BusinessFAQ, AIEmailLog

class BusinessFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessFAQ
        fields = '__all__'

class AIEmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIEmailLog
        fields = '__all__'