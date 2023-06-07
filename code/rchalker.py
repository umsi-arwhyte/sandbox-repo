import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'maul'}).json()
darth_maul = response['results'][0]

print(f"\nDarth Maul = {darth_maul}")