import requests
from django.conf import settings
from django.shortcuts import render
from datetime import datetime, timedelta
from django.core.cache import cache

def api_data_view(request):
    return render(request, 'integrations/api_data.html', {"message": "This is a placeholder for the API data view."})

def shodan_view(request):
    ip = request.GET.get('ip', '8.8.8.8')  # Default to a known IP
    url = f"https://api.shodan.io/shodan/host/{ip}?key={settings.SHODAN_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {'error': str(e)}
    return render(request, 'integrations/shodan_view.html', {'data': data})

def abuseipdb_view(request):
    ip = request.GET.get('ip', '8.8.8.8')  # Default to a known IP
    url = f"https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Accept': 'application/json',
        'Key': settings.ABUSEIPDB_API_KEY
    }
    params = {'ipAddress': ip}
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {'error': str(e)}
    return render(request, 'integrations/abuseipdb_view.html', {'data': data})

def greynoise_view(request):
    ip = request.GET.get('ip', '8.8.8.8')  # Default to a known IP
    url = f"https://api.greynoise.io/v2/noise/context/{ip}"
    headers = {
        'Accept': 'application/json',
        'key': settings.GREYNOISE_API_KEY  # Ensure you have this key in your settings
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        data = {'error': str(e)}
    return render(request, 'integrations/greynoise_view.html', {'data': data})
