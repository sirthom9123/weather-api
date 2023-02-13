import requests
from django.conf import settings


def get_coordinates(location):
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?access_token={settings.MAPBOX_KEY}')
    data = response.json()
    coordinates = data['features'][0]['center']
    return coordinates


def get_forecast(lat, lon, location):
    # Insert the coordinates and get the response from the weather api
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,alerts&mode=json&units=metric&appid=' + settings.WEATHER_API + ''
    data = requests.get(url.format(lat, lon)).json()

    forecast_data = {
            'lat': lat,
            'lon': lon,
            'location': location,
            'temperature': data['current']['temp'],
            'humidity': data['current']['humidity'],
            'wind': data['current']['wind_speed'],
            'description': data['current']['weather'][0]['description'],
            'icon': data['current']['weather'][0]['icon'],
            'hourly': data['hourly'][0]['temp'],
    }
    
    return forecast_data
    