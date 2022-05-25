import requests


endpoint = 'https://swapi.py4e.com/api'
response = requests.get(f"{endpoint}/people/", {'search': 'darth'}).json()
kt_test = response['results'][0]

print(f"\nDarth Vader = {kt_test}")