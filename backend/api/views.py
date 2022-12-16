import json 

from django.http import JsonResponse


def api_home(request, *args, **kwargs):
  request_body = request.body
  params = request.GET
  body = None
  try: body = json.loads(request_body)
  except: pass
  data = {"body": body, "params": params}
  return JsonResponse(data)
