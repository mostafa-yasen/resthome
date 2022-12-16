from products.models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict


def random_product(request, *args, **kwargs):
  random_product = Product.objects.all().order_by("?").first()
  data = {}
  if random_product: data = model_to_dict(random_product, fields=["id", "title", "price"])
  return JsonResponse(data)
