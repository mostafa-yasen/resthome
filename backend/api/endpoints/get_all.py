from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict


@api_view(["GET"])
def get_all_products(request, *args, **kwargs):
  products = Product.objects.all()
  return Response([model_to_dict(p, fields=["id", "title"]) for p in products])
