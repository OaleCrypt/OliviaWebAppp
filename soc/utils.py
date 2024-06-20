import requests

def fetch_attack_data():
    """
    Fetches the attack data from the static JSON file hosted on GitHub Pages.
    """
    url = "https://oalecrypt.github.io/Mitre_Subset_Extract/enterprise-attack-subset.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print("Fetched Data:", data[:5])  # Print the first 5 items to inspect
        return data
    except requests.RequestException as e:
        print(f"Error fetching attack data: {e}")
        return None  # Return None if there's an error
