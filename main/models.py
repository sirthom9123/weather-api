from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ForecastData(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    location = models.CharField(max_length=355)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.CharField(max_length=25)
    wind = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_date',)
        verbose_name_plural = 'Forecast Data'
        
    def __str__(self):
        return f'{self.location} - {self.temperature} degrees celcius for {self.created_date}' 
    