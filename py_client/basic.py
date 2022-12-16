import requests

from settings import BASE_URL

endpoint = BASE_URL + "/api"

response = requests.get(endpoint)

print(response.json().get("message"))
print(response.status_code)
