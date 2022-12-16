import requests

from settings import BASE_URL

endpoint = BASE_URL + "api/product/new"
params = {}
json_body = {"title": "Wired Mouse", "price": 120.00, "content": "This is a good wired mouse"}
response = requests.post(endpoint, params=params, json=json_body)

print(response.json())
print(response.status_code)
