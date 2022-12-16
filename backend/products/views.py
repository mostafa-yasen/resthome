from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from products.serializers import ProductSerializer


@api_view(["GET"])
def get_all_products(request, *args, **kwargs):
  products = Product.objects.all()
  return Response([ProductSerializer(p).data for p in products])


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer