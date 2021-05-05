import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'leia'}).json()
leia_organa = response['results'][0]

print(f"\nLeia_Organa = {leia_organa}")

