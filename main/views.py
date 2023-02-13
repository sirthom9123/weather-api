from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib import messages
import json

from .models import ForecastData
from .utils import get_coordinates, get_forecast

# Create your views here.
def main_view(request):
    # Get the location from text input
    location = request.GET.get('location')
    
    # initialize variables
    location_coord = ''
    lat = ''
    lon = ''
    forecast_data = None
    data = None
    
    if location:
        # Call util function to get coordinates from mapbox api
        location_coord = get_coordinates(location)
        lat = location_coord[1]
        lon = location_coord[0]
    
        # Call util function to get weather data
        forecast_data = get_forecast(lat, lon, location)

    
    history_data = ForecastData.objects.all()
    if history_data is not None:
        paginator = Paginator(history_data, 6)
        page = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page)
        data = {'page_obj': page_obj}
    
    context = {'forecast': forecast_data, 'data': data}
    request.session['forecast_data'] = forecast_data
    
    
    return render(request, 'main/index.html', context)


def save_forecast(request):    
    context = request.session['forecast_data'] 
  
    ForecastData.objects.create(
        latitude=context['lat'], 
        longitude=context['lon'], 
        location=context['location'],
        temperature=context['temperature'],
        humidity=context['humidity'],
        wind=context['wind'],
        description=context['description'],
        icon=context['icon']
    )        
    messages.success(request, 'Weather data saved succesfully')
    return redirect('/')


def search_data(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        forecast = ForecastData.objects.filter(
            location__icontains=search_str) | ForecastData.objects.filter(
            temperature__istartswith=search_str) | ForecastData.objects.filter(
            description__icontains=search_str) | ForecastData.objects.filter(
            created_date__icontains=search_str) 
        
        data = forecast.values()
        return JsonResponse(list(data), safe=False)
        
        
    