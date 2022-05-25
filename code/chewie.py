import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'darth'}).json()
darth_vader = response['results'][0]

print(f"\nDarth Vader = {darth_vader}")