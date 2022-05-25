import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'luke skywalker'}).json()
luke = response['results'][0]

print(f"\nLuke Skywalker = {luke}")