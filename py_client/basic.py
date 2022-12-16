import requests

from settings import BASE_URL

endpoint = BASE_URL + "api/"
params = {
  "abc": 123
}
json_body = {
  "foo": "bar"
}
response = requests.get(endpoint, params=params, json=json_body)

print(response.json())
print(response.status_code)
