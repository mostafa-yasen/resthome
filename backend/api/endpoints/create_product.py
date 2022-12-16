from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(["POST"])
def create_product(request, *args, **kwargs):
  serializer = ProductSerializer(data=request.data)
  print(request.data)
  if not serializer.is_valid(raise_exception=True):
    return Response({"error": "Bad Request", "message": "Invalid Data"}, 400)
  
  instance = serializer.save()
  return Response(serializer.data)
