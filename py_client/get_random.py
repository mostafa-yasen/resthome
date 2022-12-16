import requests

from settings import BASE_URL

endpoint = BASE_URL + "api/random"
params = {}
json_body = {}
response = requests.get(endpoint, params=params, json=json_body)

print(response.json())
print(response.status_code)
