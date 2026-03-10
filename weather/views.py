# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WeatherRequestSerializer
import os

class WeatherAPIView(APIView):
    def post(self, request):
        serializer = WeatherRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        city = serializer.validated_data['city']
        country = serializer.validated_data['country_name']
        api_key = os.environ['OWM_API_KEY']
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
        response = requests.get(url)
        
        if response.status_code != 200:
            return Response({"error": "City not found or API error"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = response.json()
        weather_data = {
            "city": data['name'],
            "country": data['sys']['country'],
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "description": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure']
        }
        return Response(weather_data)
