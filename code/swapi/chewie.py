import requests

endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'chewbacca'}).json()
chewie = response['results'][0]

print(f"\nChewbacca = {chewie}")