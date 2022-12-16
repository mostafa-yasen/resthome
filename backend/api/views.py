import json 

from django.http import JsonResponse
from .endpoints.random_product import random_product
from .endpoints.create_product import create_product

def api_home(request, *args, **kwargs):
  request_body = request.body
  params = request.GET
  body = None
  try: body = json.loads(request_body)
  except: pass
  data = {"body": body, "params": params}
  return JsonResponse(data)
