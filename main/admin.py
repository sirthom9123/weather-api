from django.contrib import admin

from .models import ForecastData

@admin.register(ForecastData)
class ForecastDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'latitude', 'longitude', 'temperature', 'humidity', 'wind', 'created_date']
    list_filter = ['temperature', 'created_date']
    search_fields = ['temperature', 'latitude']
    list_display_links = ['temperature', 'id']
    sortable_by = ['created_date', 'temperature']
