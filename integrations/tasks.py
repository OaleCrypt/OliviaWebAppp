import requests
from django.core.cache import cache
from django.conf import settings
from celery import shared_task

@shared_task
def fetch_shodan_data():
    ip = '8.8.8.8'  # Default IP or use dynamic IP as required
    url = f"https://api.shodan.io/shodan/host/{ip}?key={settings.SHODAN_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        cache.set('shodan_data', data, timeout=86400)  # Cache for 1 day
    except requests.exceptions.RequestException as e:
        cache.set('shodan_data', {'error': str(e)}, timeout=86400)

@shared_task
def fetch_abuseipdb_data():
    ip = '8.8.8.8'  # Default IP or use dynamic IP as required
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
        cache.set('abuseipdb_data', data, timeout=86400)  # Cache for 1 day
    except requests.exceptions.RequestException as e:
        cache.set('abuseipdb_data', {'error': str(e)}, timeout=86400)

@shared_task
def fetch_greynoise_data():
    ip = '8.8.8.8'  # Default IP or use dynamic IP as required
    url = f"https://api.greynoise.io/v2/noise/context/{ip}"
    headers = {
        'Accept': 'application/json',
        'key': settings.GREYNOISE_API_KEY  # Ensure you have this key in your settings
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        cache.set('greynoise_data', data, timeout=86400)  # Cache for 1 day
    except requests.exceptions.RequestException as e:
        cache.set('greynoise_data', {'error': str(e)}, timeout=86400)
