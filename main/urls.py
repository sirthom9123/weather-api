from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import main_view, save_forecast, search_data


urlpatterns = [
    path('', main_view, name='index'),
    path('save-forecast/', save_forecast, name='save_forecast'),
    path('search-data/', csrf_exempt(search_data), name='search_data'),
]
