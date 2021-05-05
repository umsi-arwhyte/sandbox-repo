import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'luke'}).json()
luke_skywalker = response['results'][0]

print(f"\nLuke Skywalker = {luke_skywalker}")