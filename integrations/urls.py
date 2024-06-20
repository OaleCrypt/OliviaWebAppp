from django.urls import path
from . import views

urlpatterns = [
    path('api-data/', views.api_data_view, name='api_data_view'),
    path('shodan/', views.shodan_view, name='shodan_view'),
    path('abuseipdb/', views.abuseipdb_view, name='abuseipdb_view'),
    path('greynoise/', views.greynoise_view, name='greynoise_view'),
]
