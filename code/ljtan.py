import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'luke'}).json()
luke_skywalker = response['results'][0]

print(f"\nLuke Skywalker = {luke_skywalker}")

response = requests.get(f"{endpoint}/people/", {'search': 'leia'}).json()
leia_organa = response['results'][0]

print(f"\nLeia Organa = {leia_organa}")

response = requests.get(f"{endpoint}/people/", {'search': 'chewbacca'}).json()
chewbacca = response['results'][0]

print(f"\nChewbacca = {chewbacca}")
