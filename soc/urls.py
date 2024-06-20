from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.alert_list_view, name='alert_list_view'),
    path('alerts/create/', views.create_alert, name='create_alert'),
    path('incidents/', views.incident_list_view, name='incident_list_view'),
    path('incidents/create/', views.create_incident, name='create_incident'),
    path('attack-map/', views.attack_map, name='attack_map'),
]
