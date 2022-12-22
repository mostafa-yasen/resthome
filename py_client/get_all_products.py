import requests

from getpass import getpass
from settings import BASE_URL

username = input('Username: ')
passwd = getpass('Password: ')

auth_response = requests.post(BASE_URL + '/api/auth', {'username': username, 'password': passwd})

if auth_response.status_code == 200:
  endpoint = BASE_URL + "api/products"
  headers = {
    'Authorization': f'Bearer {auth_response.json()["token"]}'
  }
  response = requests.get(endpoint, headers=headers)
  print(response.json())
  print(response.status_code)
else:
  print(auth_response.text)
