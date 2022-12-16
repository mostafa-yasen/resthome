from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer


@api_view(["GET"])
def get_all_products(request, *args, **kwargs):
  products = Product.objects.all()
  return Response([ProductSerializer(p).data for p in products])
