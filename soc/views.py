from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlertForm
from .incident_form import IncidentForm
from .utils import fetch_attack_data
from datetime import datetime
import json

# Temporary storage for incidents and alerts
def get_temp_incidents(request):
    return request.session.get('temp_incidents', [])

def save_temp_incident(request, incident):
    incidents = get_temp_incidents(request)
    incidents.insert(0, incident)  # Add new incident to the top of the list
    request.session['temp_incidents'] = incidents

def get_temp_alerts(request):
    return request.session.get('temp_alerts', [])

def save_temp_alert(request, alert):
    alerts = get_temp_alerts(request)
    alerts.insert(0, alert)  # Add new alert to the top of the list
    request.session['temp_alerts'] = alerts

def clear_temp_incidents(request):
    request.session['temp_incidents'] = []

def clear_temp_alerts(request):
    request.session['temp_alerts'] = []

# View to display the list of alerts
def alert_list_view(request):
    data = fetch_attack_data()
    alerts = data[:30] if data else []
    temp_alerts = get_temp_alerts(request)

    # Only include alerts with descriptions and map "source_name" to "title"
    alerts = [
        {
            'title': (alert.get('external_references', [{}])[0].get('source_name', '')[:8] + '...')
                    if len(alert.get('external_references', [{}])[0].get('source_name', '')) > 8
                    else alert.get('external_references', [{}])[0].get('source_name', 'No Title'),
            'description': alert['description'],
            'priority': 'High',  # Default to High; you can adjust based on your data
        }
        for alert in alerts if 'description' in alert and alert['description']
    ]

    # Ensure all temporary alerts have 'title', 'description', and 'priority' fields
    for temp_alert in temp_alerts:
        temp_alert.setdefault('title', 'No Title')
        temp_alert.setdefault('description', 'No description provided')
        temp_alert.setdefault('priority', 'High')

    # Only show 'priority', 'title', and 'description' in the alert list
    final_alerts = [{'priority': a['priority'], 'title': a['title'], 'description': a['description']} for a in (temp_alerts + alerts)]

    return render(request, 'soc/alert_list.html', {'alerts': final_alerts})

# View to handle the creation of new alerts
def create_alert(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            new_alert = form.cleaned_data
            # Convert datetime to string to avoid serialization issues
            if new_alert.get('date_created'):
                new_alert['date_created'] = new_alert['date_created'].strftime('%Y-%m-%d %H:%M:%S')
            save_temp_alert(request, new_alert)
            messages.success(request, 'Alert Created!')
            return redirect('alert_list_view')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = AlertForm(initial={'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    return render(request, 'soc/create_alert.html', {'form': form})

# View to display the list of incidents
def incident_list_view(request):
    data = fetch_attack_data()
    if data:
        filtered_incidents = [incident for incident in data if incident.get('description')]
        incidents = [
            {
                **incident,
                'date_created': incident.get('created', 'N/A'),
                'details': incident.get('description', ''),
            }
            for incident in filtered_incidents[:20]
        ]
        for incident in incidents[:5]:
            print("Incident Created:", incident.get('created'))
    else:
        incidents = []

    temp_incidents = get_temp_incidents(request)
    for temp_incident in temp_incidents:
        temp_incident.setdefault('created', temp_incident['date_created'])
        temp_incident.setdefault('description', temp_incident.get('details', 'No description provided'))
        temp_incident.setdefault('severity', 'Add')

    return render(request, 'soc/incident_list.html', {'incidents': temp_incidents + incidents})

# View to handle the creation of new incidents
def create_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            new_incident = form.cleaned_data
            new_incident['date_created'] = new_incident['date_created'].strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime to string
            save_temp_incident(request, new_incident)
            messages.success(request, 'Incident Created!')
            return redirect('incident_list_view')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = IncidentForm(initial={'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    return render(request, 'soc/create_incident.html', {'form': form})

# View to display the attack map
def attack_map(request):
    metrics = [
        {"Metric": "SecurityEvent", "Count": 120},
        {"Metric": "Syslog", "Count": 300},
        {"Metric": "SecurityAlert", "Count": 80},
        {"Metric": "SecurityIncident", "Count": 45},
        {"Metric": "AzureNetworkAnalytics_CL", "Count": 210},
    ]

    return render(request, 'soc/attack_map.html', {'metrics': metrics})
