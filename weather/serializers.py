# serializers.py
from rest_framework import serializers

class WeatherRequestSerializer(serializers.Serializer):
    country_name = serializers.CharField()
    city = serializers.CharField()
