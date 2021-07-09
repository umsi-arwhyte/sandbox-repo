import requests

endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'rey'}).json()
rey = response['results'][0]

print(f"\nRey = {rey}")