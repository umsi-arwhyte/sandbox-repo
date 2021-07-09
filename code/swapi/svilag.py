import requests

endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'Finn'}).json()
finn = response['results'][0]

print(f"\nFinn = {finn}")