import requests

API_KEY = "QKBRfsocc4sCpgWU4ynUcog2zTJwM7RmSs6JIAzz"
REQUEST_URL = "https://api.api-ninjas.com/v1/animals"


def extract_animals_data(search_term):
    try:
        headers = {'x-api-key': API_KEY}
        params = {'name': search_term}
        response = requests.get(REQUEST_URL, headers=headers, params=params)
        animals = response.json()
        return animals

    except requests.exceptions.ConnectionError:
        print("Connection failed")
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code == 404:
            print("Not found — check the endpoint URL")
        elif status_code >= 500:
            print("Server error — try again later")
        else:
            print(f"HTTP Error {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error: {e}")
