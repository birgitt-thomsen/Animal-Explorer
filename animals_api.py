import requests

API_KEY = "QKBRfsocc4sCpgWU4ynUcog2zTJwM7RmSs6JIAzz"
SEARCH_TERM = "fox"
REQUEST_URL = "https://api.api-ninjas.com/v1/animals"

def return_animals(search_term):
    headers = {'x-api-key': API_KEY}
    params = {'name': search_term}
    response = requests.get(REQUEST_URL, headers=headers, params=params)
    animals = response.json()
    return animals

print(return_animals(SEARCH_TERM))


