"""
Handles animals the api request to extract animal data
points.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
REQUEST_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
    ...
    },
    'locations': [
        ...
    ],
    'characteristics': {
    ...
    }
    },
    """
    try:
        headers = {'x-api-key': API_KEY}
        params = {'name': animal_name}
        response = requests.get(REQUEST_URL,
                                headers=headers,
                                params=params,
                                timeout=5)
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
