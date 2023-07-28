from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class WeatherAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        loc = request.data.get('loc')
        time = request.data.get('time')
        if not loc:
            loc = 'ha noi'
        if not time:
            time = 1
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=d927eaa5ae6390524b8720ddc018feac'
        #url = 'https://api.openweathermap.org/data/2.5/weather?id={}&appid=d927eaa5ae6390524b8720ddc018feac'
        res = requests.get(url.format(loc)).json()
        if res['cod'] == 200:
            weather_infor = {
                'Location': res['name'],
                'Country': res['sys']['country'],
                'Temperature': round(res['main']['temp'] - 273.15,2),
                'Weather': res['weather'][0]['main'],
                'Humidity':res['main']['humidity'],
                'Hressure': res['main']['pressure']
            }
            weather = {}
            if time == 1:
                weather['Today'] = weather_infor
            elif time ==2:
                weather['Next day'] = weather_infor
            elif time ==3:
                weather['Next 3 days'] = [weather_infor, weather_infor, weather_infor]
            elif time == 7:
                weather['Next 7 days'] = [weather_infor, weather_infor, weather_infor, weather_infor, weather_infor, weather_infor, weather_infor]


        return Response(weather, status=status.HTTP_200_OK)