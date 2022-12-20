import requests

from settings import BASE_URL

try: product_id = int(input("Enter product id: "))
except:
  print("Invalid product id")
  exit(1)

endpoint = BASE_URL + f"api/products/{product_id}/delete"

response = requests.delete(endpoint)
print(response.text)
print(response.status_code)
