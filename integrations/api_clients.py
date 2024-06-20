# integrations/api_clients.py
import requests
from decouple import config

# Greynoise API Client
# def fetch_greynoise_data():
#     api_key = config('GREYNOISE_API_KEY')
#     url = "https://api.greynoise.io/v2/noise/context/8.8.8.8"
#     headers = {"key": api_key}
#     response = requests.get(url, headers=headers)
#     return response.json()

# Shodan API Client
def fetch_shodan_data(ip):
    api_key = config('SHODAN_API_KEY')
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    response = requests.get(url)
    return response.json()

# AbuseIPDB API Client
def fetch_abuseipdb_data(ip):
    api_key = config('ABUSEIPDB_API_KEY')
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Accept": "application/json", "Key": api_key}
    params = {"ipAddress": ip}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# App.iogeolocation API Client
# def fetch_geolocation_data(ip):
#     api_key = config('APP_IOGEOLOCATION_API_KEY')
#     url = f"https://api.app.iogeolocation.io/ipgeo?apiKey={api_key}&ip={ip}"
#     response = requests.get(url)
#     return response.json()
